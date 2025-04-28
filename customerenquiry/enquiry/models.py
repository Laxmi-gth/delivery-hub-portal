from django.db import models
import datetime
import time

# Create your models here.
def getQueryID():
    now=datetime.datetime.now()
    return now.strftime('%Y%m%d%H%M%S') + str(now.microsecond)

class CustomerEnquiry(models.Model):
    customer_name=models.CharField(max_length=100)
    phone=models.CharField(max_length=10, blank=True)
    email=models.EmailField(max_length=200, blank=True)
    query=models.CharField(max_length=500)
    status=models.CharField(max_length=20,default='new')
    query_id=models.CharField(primary_key=True,max_length=30,default=getQueryID)

def __str__(self):
    return f"{self.customer_name} - {self.query_id}"




