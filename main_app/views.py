from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1>Life Ledger</h1>')

def about(request):
    return HttpResponse('<h2>Learn more<h2>')