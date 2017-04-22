from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Customer(models.Model):
    customerID = models.IntegerField(primary_key=True)
    fName = models.CharField(max_length=500)
    lName = models.CharField(max_length=100)
    joinDate = models.CharField(max_length=1000)
    primaryEmailID = models.CharField(max_length=1000)
    preferEmail = models.BooleanField(default=True)
    emailNotification = models.BooleanField()
    billType = models.CharField(max_length=20)
    contactNo = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    def get_absolute_url(self):
        return reverse('Customer:home')
    def __str__(self):
        return self.fName +" "+ self.lName

class Service_Request(models.Model):
    customerID = models.ForeignKey(Customer,on_delete=models.CASCADE)
    requestID = models.IntegerField(primary_key=True)
    requestType = models.CharField(max_length=500)
    subscriptionDate = models.CharField(max_length=100)
    fulfillmentDate = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)

class Shipping_Address(models.Model):
    customerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    shipAddID = models.IntegerField(primary_key=True)
    state = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    zip = models.CharField(max_length=10)
    street = models.CharField(max_length=100)



class Payment_Method(models.Model):
    customerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    pmtMethodID = models.IntegerField(primary_key=True)
    cardNo = models.CharField(max_length=100)
    cardHolderName = models.CharField(max_length=20)
    cardType = models.CharField(max_length=50)
    expDate = models.CharField(max_length=20)
    cvvNo = models.IntegerField()
    def __str__(self):
        return self.cardHolderName +"-"+ self.cardNo

class Billing_Address(models.Model):
    PmtMethodID = models.ForeignKey(Payment_Method, on_delete=models.CASCADE)
    billAddID = models.IntegerField(primary_key=True)
    state = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    zip = models.CharField(max_length=10)
    street = models.CharField(max_length=100)

class Security (models.Model):
    qID = models.IntegerField(primary_key=True)
    customerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    question = models.CharField(max_length=1000)
    answer = models.CharField(max_length=1000)

class Product_type(models.Model):
    productID = models.IntegerField(primary_key=True)
    productType = models.CharField(max_length=100)

class Settings_of_interst(models.Model):
    productID = models.ForeignKey(Product_type, on_delete=models.CASCADE)
    customerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    interestID = models.IntegerField(primary_key=True)
#class Song(models.Model):
#   album = models.ForeignKey(Album, on_delete=models.CASCADE)
#   file_type = models.CharField(max_length=10)
#   song_title = models.CharField(max_length=250)