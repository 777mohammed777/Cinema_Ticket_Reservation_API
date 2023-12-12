from django.db import models

# Create your models here.


class Movie(models.Model):
    hall=models.CharField(max_length=100)
    movie=models.CharField(max_length=100)
    
class Guest(models.Model):
    name=models.CharField(max_length=100)
    mobile=models.CharField(max_length=11)
    
class Resevation(models.Model):
    guest=models.ForeignKey(Guest,related_name="reservation" , on_delete=models.CASCADE)
    movie=models.ForeignKey(Movie,related_name="reservation" , on_delete=models.CASCADE)