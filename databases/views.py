# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import sample


def showform(request):
    if request.method == 'POST':
         form = sample(request.POST)
    else:
         form = sample()
    
    return render(request, 'databases/temp.html', {'form': form})    


def db(request):
    if request.method == 'POST':
        form = sample(request.POST)
        #  form.save()
        name = request.POST.get('name')
        user_id = request.POST.get('user_id')
        num1 = request.POST.get('num1')
        num2 = request.POST.get('num2')
        num3 = request.POST.get('num3') 
        f=sample(name=request.POST.get('name'),user_id = request.POST.get('user_id'),num1 = request.POST.get('num1'),num2 = request.POST.get('num2'),num3 = request.POST.get('num3'))
        f.save()    
    var = sample.objects.values()
    print var
    return HttpResponse(var)