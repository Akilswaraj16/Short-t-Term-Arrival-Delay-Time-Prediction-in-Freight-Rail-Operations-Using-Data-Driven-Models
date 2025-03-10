from django.db import models

# Create your models here.
from django.db.models import CASCADE


class ClientRegister_Model(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    gender= models.CharField(max_length=30)
    address= models.CharField(max_length=30)


class delay_prediction_type(models.Model):

    ddatetime= models.CharField(max_length=300)
    idn= models.CharField(max_length=300)
    carrier = models.CharField(max_length=300)
    adate1= models.CharField(max_length=300)
    connection= models.CharField(max_length=300)
    arrival= models.CharField(max_length=300)
    delay_in_min= models.CharField(max_length=300)
    name= models.CharField(max_length=300)
    Prediction= models.CharField(max_length=300)

class detection_accuracy(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)

class detection_ratio(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)



