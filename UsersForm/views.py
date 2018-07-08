# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render

from .models import Users
from .forms import UserForm


def home(request):
    return render(request, 'home.html', {})


def list(request):
    users = Users.objects.all()
    resp = []
    for user in users:
        user = {'name': user.name, 'email': user.email}
        resp.append(user)
    return JsonResponse(resp, safe=False)


def add(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = Users(name=request.POST['name'], email=request.POST['email'])
            user.save()
            return HttpResponseRedirect('/list/')
    else:
        form = UserForm()
    return render(request, 'add.html', {'form': form})
