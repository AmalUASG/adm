from django.db import models
# from datetime import date
from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.conf import settings
import pyodbc
from django.contrib.auth.models import AbstractUser
import logging

# from azure_signin.backends import AzureSigninBackend

logger = logging.getLogger(__name__)

# class All(models.Model):
#     class Meta:
#         db_table = 'All'
#         managed = False
#     id= models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
#     # id = models.BigAutoField(primary_key=True)
#     DD_PR_KDBUSER = models.CharField(db_column='DD_PR_KDBUSER', max_length=20)  # Field name made lowercase.
#     DD_PR_KDBTIME = models.CharField(db_column='DD_PR_KDBTIME', max_length=20)
#     DD_PR_PRICELIST = models.CharField(db_column='DD_PR_PRICELIST', max_length=20)
#     DD_PR_MANUFACT = models.CharField(db_column='DD_PR_MANUFACT', max_length=20)
#     DD_PR_MODEL = models.CharField(db_column='DD_PR_MODEL', max_length=20)
#     DD_PR_VARIANT = models.CharField(db_column='DD_PR_VARIANT', max_length=20)
#     DD_PR_SUBVARIANT = models.CharField(db_column='DD_PR_SUBVARIANT', max_length=20)
#     DD_PR_OTYPE = models.CharField(db_column='DD_PR_OTYPE', max_length=20)
#     DD_PR_OPTION = models.CharField(db_column='DD_PR_OPTION', max_length=20)
#     DD_PR_FRDATE = models.CharField(db_column='DD_PR_FRDATE', max_length=20)
#     DD_PR_TODATE = models.CharField(db_column='DD_PR_TODATE', max_length=20)
#     DD_PR_OPTIONID = models.CharField(db_column='DD_PR_OPTIONID', max_length=20)
#     DD_PR_TAXGROUP = models.CharField(db_column='DD_PR_TAXGROUP', max_length=20)
#     DD_PR_PRICE = models.CharField(db_column='DD_PR_PRICE', max_length=20)
#     DD_PR_CARTAXCODE = models.CharField(db_column='DD_PR_CARTAXCODE', max_length=20)
#     DD_PR_CARTAXVALUE = models.CharField(db_column='DD_PR_CARTAXVALUE', max_length=20)
#     DD_PR_VATINCLPRICE = models.CharField(db_column='DD_PR_VATINCLPRICE', max_length=20)
#     DD_PR_XS_BMW_FIXPRICE = models.CharField(db_column='DD_PR_XS_BMW_FIXPRICE', max_length=20)


    


# class Maintenance(models.Model) : 
#     class Meta:
#         db_table = 'Maintenance'

#     DD_PR_KDBUSER = models.CharField(db_column='DD_PR_KDBUSER', max_length=20, null=True)  # Field name made lowercase.
#     DD_PR_KDBTIME = models.CharField(db_column='DD_PR_KDBTIME', max_length=20, null=True)
#     DD_PR_PRICELIST = models.CharField(db_column='DD_PR_PRICELIST', max_length=20, null=True)
#     DD_PR_MANUFACT = models.CharField(db_column='DD_PR_MANUFACT', max_length=20, null=True)
#     DD_PR_MODEL = models.CharField(db_column='DD_PR_MODEL', max_length=20, null=True)
#     DD_PR_VARIANT = models.CharField(db_column='DD_PR_VARIANT', max_length=20, null=True)
#     DD_PR_SUBVARIANT = models.CharField(db_column='DD_PR_SUBVARIANT', max_length=20, null=True)
#     DD_PR_OTYPE = models.CharField(db_column='DD_PR_OTYPE', max_length=20, null=True)
#     DD_PR_OPTION = models.CharField(db_column='DD_PR_OPTION', max_length=20, null=True)
#     DD_PR_FRDATE = models.CharField(db_column='DD_PR_FRDATE', max_length=20, null=True)
#     DD_PR_TODATE = models.CharField(db_column='DD_PR_TODATE', max_length=20, null=True)
#     DD_PR_OPTIONID = models.CharField(db_column='DD_PR_OPTIONID', max_length=20, null=True)
#     DD_PR_TAXGROUP = models.CharField(db_column='DD_PR_TAXGROUP', max_length=20, null=True)
#     DD_PR_PRICE = models.CharField(db_column='DD_PR_PRICE', max_length=20, null=True)
#     DD_PR_CARTAXCODE = models.CharField(db_column='DD_PR_CARTAXCODE', max_length=20, null=True)
#     DD_PR_CARTAXVALUE = models.CharField(db_column='DD_PR_CARTAXVALUE', max_length=20, null=True)
#     DD_PR_VATINCLPRICE = models.CharField(db_column='DD_PR_VATINCLPRICE', max_length=20, null=True)
#     DD_PR_XS_BMW_FIXPRICE = models.CharField(db_column='DD_PR_XS_BMW_FIXPRICE', max_length=20, null=True)









class Manufact(models.Model) : 
    
    def __str__(self):
            return self.manufact

    description = models.CharField( max_length=20, null=True) 
    manufact = models.CharField(max_length=20, null=True)

    class Meta:
        db_table = 'Manufact'

    


class Model(models.Model) : 
    
    def __str__(self):
            return self.model

    model = models.CharField( max_length=20, null=True) 
    manufact =  models.CharField( null=True)
    description = models.CharField(  null=True)

    class Meta:
        db_table = 'Model'




class Variant(models.Model) : 
    
    def __str__(self):
            return self.variant

    manufact = models.CharField( max_length=20, null=True) 
    model =  models.CharField( null=True)
    variant =  models.CharField( null=True)
    description =  models.CharField( null=True)
    cc =  models.CharField( null=True)
    locator =  models.CharField( null=True)

    class Meta:
        db_table = 'Variant'





class Price(models.Model) : 
    
    def __str__(self):
            return self.variant
    
    pricelist = models.CharField( max_length=20, null=True) 
    manufact = models.CharField( max_length=20, null=True) 
    model =  models.CharField( null=True)
    variant =  models.CharField( null=True)
    price =  models.CharField( null=True)


    class Meta:
        db_table = 'Price'



class VM_10_VSPEC(models.Model) : 
    
    def __str__(self):
            return self.variant
    
    kdbtime = models.DateTimeField(null=True) 
    manufact = models.CharField( null=True) 
    model =  models.CharField( null=True)
    variant =  models.CharField( null=True)
    options = models.CharField(null=True)
    desciption =  models.CharField( null=True)


    class Meta:
        db_table = 'VM_10_VSPEC'



# class ExtendedUser(User):
#     """
#     Extend user with extra attributes set in `AZURE_SIGNIN["RENAME_ATTRIBUTES"]`
#     """

#     emaila = models.EmailField(unique=True, db_index=True)
#     employee_id = models.IntegerField(
#         null=True, default=None, unique=True, blank=True, db_index=True
#     )
#     omk2 = models.CharField(max_length=5, null=True, default=None, db_index=True)
#     hcm = models.CharField(max_length=7, null=True, default=None, db_index=True)


# class CustomAzureSigninBackend(AzureSigninBackend):
#     "Subclass AzureSigninBackend to customize validation rules for user."

#     def is_valid_user(self, user: dict, *args, **kwargs) -> bool:
#         "is_valid_user"
#         output = super().is_valid_user(user, *args, **kwargs)
#         try:
#             "run extra checks here..."
#             pass
#         except Exception as e:
#             logger.exception(e)
#         logger.debug("is_valid_user: %s", output)
#         return output