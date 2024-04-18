from django.shortcuts import render
from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import uuid
from .mail import*
# Create your views here.
def admin_page(request):
    data=Product.objects.all()
    context={
        'Data':data
    }
    return render(request,"firstPage/admin.html",context)

@login_required(login_url='login/')
def firstpage(request):
    data=Product.objects.all()
    if request.GET.get('search'):
        data=data.filter(name__icontains = request.GET.get('search'))
    else:
        data=Product.objects.all()
    
    context={
        'Data':data
    }
    return render(request,"firstPage/firstpage.html",context)

def add_product(request):
    if request.method=='POST':
        data=request.POST
        img=request.FILES.get('pic')
        name=data.get('name')
        desc=data.get('desc')
        print(img,name,desc)
        Product.objects.create(
            name=name,
            desc=desc,
            pic=img,
        )
        return redirect('/admin/add_product')

    return render(request,"firstPage/addproduct.html")

def prod_page(request,uuid):
        value=Product.objects.all().get(uuid=uuid)
        context={
             "info":value
        }
        return render(request,"firstPage/product.html",context)

def req_product(request):
    if request.method=='POST':
        data=request.POST
        img=request.FILES.get('pic')
        name=data.get('name')
        desc=data.get('desc')
        value=Requested_Product.objects.create(
        name=name,
        desc=desc,
        pic=img,
        )
        send_requested_product(value)
    return render(request,"firstPage/addproduct.html")