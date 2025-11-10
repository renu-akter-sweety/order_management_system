from django.db import models

# Create your models here.
class customermodel(models.Model):
    customer_name=models.CharField(max_length=100, null=True)
    email=models.EmailField(null=True)
    phone=models.CharField(max_length=15,null=True)
    address=models.TextField(null=True)
    def __str__(self):
        return self.customer_name
    


class ordermodel(models.Model):
    customer= models.ForeignKey(customermodel, related_name='customer_info', on_delete=models.CASCADE)   
    product_name=models.CharField(max_length=100, null=True)
    unit_price=models.FloatField(null=True)
    quantity=models.CharField(max_length=100, null=True)
    discount_percent=models.FloatField(null=True)
    tax_percent=models.FloatField(null=True)

    subtotal=models.FloatField(default=0)
    discount_amount=models.FloatField(default=0)
    tax_amount=models.FloatField(default=0)
    total_amount=models.FloatField(default=0)
