from django.db import models


# Create your models here.


class Customer( models.Model ):
    name = models.CharField( max_length=100 )
    email = models.EmailField(unique=True)
    created_date = models.DateTimeField( auto_now_add=True )

    def __str__(self):
        return f"{self.id} - {self.name} - {self.email} - {self.created_date}"


class CsvProduct(models.Model):
    title = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    customer = models.ForeignKey(to=Customer,on_delete=models.PROTECT)
    uploaded_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  f"{self.id} {self.title} {self.customer.id} {self.price}"
