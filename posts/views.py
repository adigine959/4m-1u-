import datetime
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hello (request):
    return render(request, 'hello.html')
def good (request):
    return render(request, 'good.html')
def h (request):
    date = datetime.datetime.now()
    return render(request, 'h.html', {'date':date})

