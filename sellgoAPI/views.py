from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from sellgoAPI.models import Customer
from sellgoAPI.serializers import CustomerSerializer


@api_view( ['POST'] )
def add_customer(request):
    try:
        customer_obj = Customer.objects.get( email=request.POST['email'] )
        response = {
            "message": "Welcome back",
            "status": status.HTTP_200_OK,
            "Student": {
                "id": customer_obj.id,
                "email": customer_obj.email
            }
        }
        return Response( response, status=status.HTTP_200_OK )
    except:
        try:
            name = request.POST.get( 'name' )
            email = request.POST.get( 'email' )
            customer_obj = Customer( name=name, email=email)
            customer_obj.save()
            message = "Customer Created!"
            httpStatus = status.HTTP_201_CREATED
        except Exception as e:
            message = str( e )
            httpStatus = status.HTTP_400_BAD_REQUEST
    response = {
        "message": message,
        "status": httpStatus,
        "Customer": {
           Customer.objects.filter(email=email).values()
        }
    }

    return Response( response, status=httpStatus )