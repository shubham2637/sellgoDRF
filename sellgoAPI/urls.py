from django.urls import path

from . import views

urlpatterns = [
    path('addcustomer',views.add_customer,name="Add Customer")
]