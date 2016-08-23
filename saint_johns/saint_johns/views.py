from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from . import models
from . import logic
from datetime import date


def home_page(request):
    '''Navigates to login page.'''
    return render(request, 'saint_johns/home.html')