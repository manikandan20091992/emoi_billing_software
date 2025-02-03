from django.db import models

201# Create your models here.
class superadminRegister(models.Model):
    username = models.TextField(blank=True,null=True)
    password = models.TextField(blank=True,null=True)
    name = models.TextField(blank=True,null=True)
    email = models.TextField(blank=True,null=True)
    datetime = models.TextField(blank=True,null=True)
    rollid = models.TextField(blank=True,null=True)

class billingAgentRegister(models.Model):
    username = models.TextField(blank=True,null=True)
    password = models.TextField(blank=True,null=True)
    name = models.TextField(blank=True,null=True)
    email = models.TextField(blank=True,null=True)
    datetime = models.TextField(blank=True,null=True)
    rollid = models.TextField(blank=True,null=True)
    
class FunctioninformationRegistertable(models.Model):
    ManaMaganName = models.TextField(blank=True,null=True)
    ManaMagalName = models.TextField(blank=True,null=True)
    FucntionDate = models.TextField(blank=True,null=True)
    FucntionLocationAddress = models.TextField(blank=True,null=True)
    billingAgentPrimarykey = models.TextField(blank=True,null=True)

class MoiDetails(models.Model):
    Moi_user_Name = models.TextField(blank=True,null=True)
    Moi_user_address= models.TextField(blank=True,null=True)
    Moi_user_occupation= models.TextField(blank=True,null=True)
    Moi_user_amount= models.TextField(blank=True,null=True)
    FunctionInformationPrimaryKey = models.TextField(blank=True,null=True)
    Moidetails_Datetime = models.TextField(blank=True,null=True)