from django import forms
from django.db.models import fields

from .models import STT,COT,STCOT, Dept,PRof,PRCO,PREREQ,AVERAGE

class STTFORM(forms.ModelForm):
    class Meta:
        model = STT
        fields = ['STID','STNAME','STLEV','STMJR','STDEID']
        


class COTFORM(forms.ModelForm):
    class Meta:
        model = COT
        fields = ['COID','COTITLE','COTYPE','CREDIT','CODEID']
        

class STCOTFORM(forms.ModelForm):
    class Meta:
        model = STCOT
        fields = ['STID','COID','TR','YRYR','Grade']
        

class PRofFORM(forms.ModelForm):
    class Meta:
        model = PRof
        fields = ['PRID','PRNAME','RANK','Special','DEID']
        
        

class PRCOFORM(forms.ModelForm):
    class Meta:
        model = PRCO
        fields = ['COID','PRID','TR','YRYR','GroupID']
        

class DeptFORM(forms.ModelForm):
    class Meta:
        model = Dept
        fields = ['DEID','DETITLE','phone','address','MGRID']
        

class PREREQFORM(forms.ModelForm):
    class Meta:  
        model = PREREQ
        fields = ['COID','PRECOID']


# class AVERAGEFORM(forms.ModelForm):
#     class Meta:
#         model = AVERAGE
#         fields = ['STNAME','STID','AVE']
        