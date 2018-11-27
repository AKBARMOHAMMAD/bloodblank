from django.db import models

# Create your models here.
class State(models.Model):
    idno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
class City(models.Model):
    idno=models.IntegerField(primary_key=True)
    state_name=models.ForeignKey(State,on_delete=models.CASCADE)
    city_name=models.CharField(max_length=50)
class DonorRegister(models.Model):
    name=models.CharField(max_length=50)
    contact_no=models.IntegerField()
    city_name=models.ForeignKey(City,on_delete=models.CASCADE)
    email_id=models.EmailField(max_length=50,primary_key=True)
    password=models.CharField(max_length=50)
class OriganizationRegister(models.Model):
    name=models.CharField(max_length=50)
    contact_no=models.IntegerField()
    city_name=models.ForeignKey(City,on_delete=models.CASCADE)
    email_id=models.EmailField(max_length=50,primary_key=True)
    password=models.CharField(max_length=50)
