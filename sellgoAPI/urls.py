from django.urls import path

from . import views

urlpatterns = [
    path('addcustomer',views.add_customer,name="Add Customer"),
    path('uploadcsv',views.uploadcsv,name="Add product csv"),
    path('getproduct',views.getproductBycustomer,name="Add product csv"),
    #test comment git push
]