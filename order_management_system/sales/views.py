from django.shortcuts import render,redirect
from sales.models import *
from sales.forms import *
# Create your views here.
def customerpage(request):

    customer_data=customermodel.objects.all()
    if request.method=='POST':
        from_data=customermodel_form(request.POST)
        if from_data.is_valid():
            from_data.save()
        return redirect('customerpage')
    else:
        from_data=customermodel_form()
    context={
        "from_data":from_data,
        'customer_data':customer_data   , 
      }
    return render(request,'customer.html',context)    
def editcustomerpage(request,id):
    customer_data=customermodel.objects.get(id=id)
    if request.method=='POST':
        from_data=customermodel_form(request.POST,instance=customer_data)
        if from_data.is_valid():
            from_data.save()
        return redirect('customerpage')
    else:
        from_data=customermodel_form(instance=customer_data)
    context={
        "from_data":from_data,
        'customer_data':customermodel.objects.all()   , 
    }
    return render(request,'customer.html',context)  

def deletecustomerpage(request,id):
    customermodel.objects.get(id=id).delete()

    return redirect('customerpage')
#order

def orderpage(request):
    data=ordermodel.objects.all()
  
    if request.method=='POST':
        order_from_data=ordermodel_form(request.POST)
        if order_from_data.is_valid():
            
            form_data=order_from_data.save(commit=False)
            subtotal = float(form_data.unit_price)*int(form_data.quantity)
            Discount_Amount =(subtotal * form_data.discount_percent)/100
            tax_amount = ((subtotal-Discount_Amount)* form_data.tax_percent)/100
            total_amount=(subtotal-Discount_Amount)+tax_amount

            form_data.subtotal=subtotal
            form_data.discount_amount=Discount_Amount
            form_data.tax_amount=tax_amount
            form_data.total_amount=total_amount
            form_data.save()

            return redirect('orderpage')
    else:
         order_from_data=ordermodel_form()  


    context={
        'order_from_data':order_from_data,
        'data':data,
    }      

    return render(request,"order.html",context)
