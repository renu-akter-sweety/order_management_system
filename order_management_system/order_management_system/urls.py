
from django.contrib import admin
from django.urls import path
from  sales.views import *
urlpatterns =[
    path('admin/', admin.site.urls),
    #customer
    path('customerpage/', customerpage, name='customerpage'),
     path('editcustomerpage/<int:id>/', editcustomerpage, name='editcustomerpage'),
     path('deletecustomerpage/<int:id>/', deletecustomerpage, name='deletecustomerpage'),
     #order
    path('orderpage/', orderpage, name='orderpage'),


]
