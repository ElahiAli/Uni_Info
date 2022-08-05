from django.db import models
from django.db.models.fields import AutoField

# Create your models here.
class STT(models.Model):
    STID   = models.CharField(primary_key=True , max_length=10)
    STNAME = models.CharField(max_length=50)
    STLEV  = models.CharField(max_length=6 , null=True , blank=False)
    STMJR  = models.CharField(max_length=10 , null=True , blank=False)
    STDEID = models.CharField(max_length=10 , null=True , blank=False)


class COT(models.Model):
    COID    = models.CharField(primary_key=True , max_length=10)
    COTITLE = models.CharField(max_length=50)
    COTYPE  = models.CharField(max_length=6 , null=True , blank=False)
    CREDIT  = models.DecimalField(decimal_places=0, max_digits=10, null=True, blank=False)
    CODEID  = models.CharField(max_length=10, null=True, blank=False) 


class Dept(models.Model):
    DEID    = models.CharField(primary_key=True , max_length=10)
    DETITLE = models.CharField(max_length=50)
    phone   = models.CharField(max_length=12, null=True, blank=False)
    address = models.CharField(max_length=10, null=True, blank=False)
    MGRID   = models.CharField(max_length=10)


class PRof(models.Model):
    PRID    = models.CharField(primary_key=True , max_length=10)
    PRNAME  = models.CharField(max_length=50)
    RANK    = models.CharField(max_length=10)
    Special = models.CharField(max_length=50, null=True, blank=False)
    DEID    = models.ForeignKey(Dept, to_field="DEID", db_column="DEID", on_delete=models.CASCADE, null=True, blank=False )


class STCOT(models.Model):
    STID  = models.ForeignKey(STT, to_field="STID", db_column="STID", on_delete=models.CASCADE)
    COID  = models.ForeignKey(COT, to_field="COID", db_column="COID", on_delete=models.CASCADE)
    TR    = models.DecimalField(decimal_places=0, max_digits=10)
    YRYR  = models.CharField(max_length=10)
    Grade = models.DecimalField(decimal_places=1, max_digits=10, null=True, blank=False)
    class Meta:
        unique_together = (("STID" , "COID"),)


class PRCO(models.Model):
    COID    = models.ForeignKey(COT, to_field="COID", db_column="COID", on_delete=models.CASCADE)
    PRID    =  models.ForeignKey(PRof, to_field="PRID", db_column="PRID", on_delete=models.CASCADE)
    TR      = models.DecimalField(decimal_places=0, max_digits=10)
    YRYR    = models.CharField(max_length=10)
    GroupID = models.CharField(max_length=10)
    class Meta:
        unique_together = (("COID" , "PRID"),)


class PREREQ(models.Model):

    COID    = models.ForeignKey(COT, to_field="COID", db_column="COID", on_delete=models.CASCADE, primary_key=True)
    PRECOID = models.CharField(max_length=10)
    
class AVERAGE(models.Model):
    STNAME = models.CharField(primary_key=True, max_length=50)
    STID   = models.CharField(max_length=10)
    AVE    = models.DecimalField(decimal_places=1, max_digits=2, null=True, blank=False)
    

