from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Context, loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

def Home(request):
    return HttpResponse('Home')

def Account(request):
    return HttpResponse('Account')
