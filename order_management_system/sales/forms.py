from django import forms
from sales.models import *



class customermodel_form(forms.ModelForm):
    class Meta:
        model=customermodel
        fields= "__all__"
     


class ordermodel_form(forms.ModelForm):
    class Meta:
        model=ordermodel
        fields= '__all__'
        exclude=[
            'sub_total','discount_amount','tax_amount','total_amount'
        ]