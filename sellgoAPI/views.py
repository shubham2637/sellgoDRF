from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from sellgoAPI.models import Customer
from sellgoAPI.serializers import CustomerSerializer,CsvProductSerializer
from .csvutils import csvToModel


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
            name = request.POST['name']
            email = request.POST['email']
            customer_obj = Customer( name=name, email=email )
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
            Customer.objects.filter( email=email ).values()
        }
    }

    return Response( response, status=httpStatus )


@api_view( ['POST'] )
def uploadcsv(request):
    try:
        try:
            customer_id = request.POST['customer_id']
            product_csv = request.FILES['product_csv']
            CustomerObj = Customer.objects.get( id=customer_id )
        except Exception as e:
            message = str( e )
            httpStatus = status.HTTP_400_BAD_REQUEST
            return Response( message, status=httpStatus )
        try:
            csvToModel( product_csv, customer=CustomerObj )
        except Exception as e:
            message = str( e )
            return Response( message, status=status.HTTP_409_CONFLICT )
    except Exception as e:
        message = str( e )
        return Response( message, status=status.HTTP_500_INTERNAL_SERVER_ERROR )
    return Response("Product added Successfully" , status.HTTP_201_CREATED)


@api_view( ['GET'] )
def getproductBycustomer(request):
    try:
        customer_id = request.POST['customer_id']
    except Exception as e:
        message = str( e )
        httpStatus = status.HTTP_404_NOT_FOUND
        Response( message, status=httpStatus )
