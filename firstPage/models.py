from typing import Any
from django.db import models as m
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Product(m.Model):
    uuid=m.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    user=m.ForeignKey(User,on_delete=m.SET_NULL,null=True,blank=True)
    name=m.CharField(max_length=100)
    desc=m.TextField()
    pic=m.ImageField(upload_to="pictures")

class Requested_Product(m.Model):
    uuid=m.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    user=m.ForeignKey(User,on_delete=m.SET_NULL,null=True,blank=True)
    name=m.CharField(max_length=100)
    desc=m.TextField()
    pic=m.ImageField(upload_to="requsted_pictures")