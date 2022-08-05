from django.db.models import query
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import  STTFORM,COTFORM,STCOTFORM,PRofFORM,PRCOFORM,DeptFORM,PREREQFORM
from .models import AVERAGE, COT, PRCO, STCOT, PRof, STT, PREREQ, Dept
# Create your views here.
def index(request):
    context = {}
    return render(request,'sirs/index.html',context)


def all_info(request):
    stt = STT.objects.all()
    cot = COT.objects.all()
    stcot = STCOT.objects.all()
    prof = PRof.objects.all()
    prco = PRCO.objects.all()
    prereq = PREREQ.objects.all()
    dept = Dept.objects.all()
    context = {
        'stt':stt,
        'cot':cot,
        'stcot':stcot,
        'prof':prof,
        'prco':prco,
        'dept':dept,
        'prereq':prereq
    }

    return render(request,'sirs/all_info.html',context)

def new_stt(request):
    if request.method != 'POST':
        form = STTFORM()
    else:
        form = STTFORM(request.POST)
        if form.is_valid():
            new_data = form.save(commit=False)
            new_data.save()
            return HttpResponseRedirect(reverse('sirs:all_info'))
        
    context = {'form':form}
    return render(request,'sirs/new_stt.html',context)


def new_cot(request):
    if request.method != 'POST':
        form = COTFORM()
    else:
        form = COTFORM(request.POST)
        if form.is_valid():
            new_data = form.save(commit=False)
            new_data.save()
            return HttpResponseRedirect(reverse('sirs:all_info'))
    
    context = {'form':form}
    return render(request,'sirs/new_cot.html',context)


def new_stcot(request):
    if request.method != 'POST':
        form = STCOTFORM()
    else:
        form = STCOTFORM(request.POST)
        if form.is_valid():
            new_data = form.save(commit=False)
            new_data.save()
            return HttpResponseRedirect(reverse('sirs:all_info'))
    
    context = {'form':form}
    return render(request,'sirs/new_stcot.html',context)


def new_prof(request):
    if request.method != 'POST':
        form = PRofFORM()
    else:
        form = PRofFORM(request.POST)
        if form.is_valid():
            new_data = form.save(commit=False)
            new_data.save()
            return HttpResponseRedirect(reverse('sirs:all_info'))
    
    context = {'form':form}
    return render(request,'sirs/new_prof.html',context)


def new_prco(request):
    if request.method != 'POST':
        form = PRCOFORM()
    else:
        form = PRCOFORM(request.POST)
        if form.is_valid():
            new_data = form.save(commit=False)
            new_data.save()
            return HttpResponseRedirect(reverse('sirs:all_info'))
    
    context = {'form':form}
    return render(request,'sirs/new_prco.html',context)


def new_dept(request):
    if request.method != 'POST':
        form = DeptFORM()
    else:
        form = DeptFORM(request.POST)
        if form.is_valid():
            new_data = form.save(commit=False)
            new_data.save()
            return HttpResponseRedirect(reverse('sirs:all_info'))
    
    context = {'form':form}
    return render(request,'sirs/new_dept.html',context)


def new_prereq(request):
    if request.method != 'POST':
        form = PREREQFORM()
    else:
        form = PREREQFORM(request.POST)
        if form.is_valid():
            new_data = form.save(commit=False)
            new_data.save()
            return HttpResponseRedirect(reverse('sirs:all_info'))
    
    context = {'form':form}
    return render(request,'sirs/new_prereq.html',context)


def average(request):
    
    all = AVERAGE.objects.all()
    
    ave = AVERAGE.objects.raw(""" select sirs_stt.STNAME,sirs_stt.STID,
        sum(sirs_stcot.Grade*sirs_cot.CREDIT)/sum(sirs_cot.CREDIT) as AVE from
        sirs_stt,sirs_cot,sirs_stcot
        where sirs_stt.STID = sirs_stcot.STID and sirs_cot.COID = sirs_stcot.COID
        group by sirs_stt.STNAME,sirs_stt.STID """)

    context = {'ave':ave , 'all':all}
    return render(request,'sirs/ave.html',context) 



def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        #stt = STT.objects.filter(STNAME__contains=searched)
        stt   = STT.objects.filter(STID__contains=searched)
        cot   = COT.objects.filter(COID__contains=searched)
        stcot = STCOT.objects.filter(STID__STID__icontains=searched)
        prof  = PRof.objects.filter(PRID__contains=searched)
        prco  = PRCO.objects.filter(PRID__PRID__icontains=searched)

        context = {'searched':searched , 'stt':stt , 'cot':cot, 'stcot':stcot , 'prof':prof , 'prco':prco}
    return render(request,'sirs/search.html',context)