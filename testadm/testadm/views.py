from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Manufact , Model , Variant , Price , VM_10_VSPEC
from datetime import datetime
import pyodbc


# from azure_signin.decorators import azure_signin_required
from django.shortcuts import HttpResponse

def addmanufact(request):
  
    cnxn = pyodbc.connect(DSN="KEYLOOP1")
    cursor = cnxn.cursor()
    c= cursor.execute("select * from DD_00_MANUF")
    row = cursor.fetchall()
    for r in row :
         
        Manufact.objects.create(description = r[0],manufact= r[7] )


        

def addmodel(request):
  
    
    cnxn = pyodbc.connect("DSN=KEYLOOP1")
    cursor = cnxn.cursor()
    c= cursor.execute("select * from DD_00_MODEL")
    row = cursor.fetchall()
    for r in row :
         
        Model.objects.create(manufact = r[0],model= r[1],description=r[2] )



def addvariant(request):
  
    
    cnxn = pyodbc.connect("DSN=KEYLOOP1")
    cursor = cnxn.cursor()
    c= cursor.execute("select * from DD_00_VARIANT")
    row = cursor.fetchall()
    for r in row :
         
        Variant.objects.create(manufact = r[0],model= r[1],variant=r[2],description=r[3],cc=r[5],locator= r[7])



def addprice(request):
  
    
    cnxn = pyodbc.connect("DSN=KEYLOOP1")
    cursor = cnxn.cursor()
    c= cursor.execute("select * from DD_01_PRICE")
    row = cursor.fetchall()
    for r in row :
         
        Price.objects.create(pricelist = r[2],manufact= r[3],model=r[4],variant=r[5],price=r[13])

def addspecialization(request):
    
    cnxn = pyodbc.connect("DSN=KEYLOOP1")
    cursor = cnxn.cursor()
    c= cursor.execute("select * from VM_10_VSPEC")
    row = cursor.fetchall()

   
    for r in row :

        VM_10_VSPEC.objects.create(kdbtime = r[1], manufact = r[2],model = r[3] ,  variant = r[4], options = r[7],desciption = r[8])



# @azure_signin_required
# def protected_view(request):
#     return HttpResponse("A view protected by the decorator")