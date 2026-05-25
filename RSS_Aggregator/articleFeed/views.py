from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Articles

# Create your views here.
def home(request):
    return render(request,  'articleFeed/index.html')