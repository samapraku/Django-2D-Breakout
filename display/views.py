from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

# Create your views here.
def index(request):
    return render(request, 'display/index.html', {})

def control(request):
    return render(request, 'display/control.html', {})
