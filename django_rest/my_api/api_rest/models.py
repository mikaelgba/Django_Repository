from django.db import models

# Create your models here.

class Hq(models.Model): 

    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    publishing = models.CharField(max_length=100)

    #create - Post
    #Recretive - Get
    #Update - Put
    #Delete - Delete