from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<p>Home view</p>')

def pet_detail(request, id):
    return HttpResponse('<p>Pet Detail view with the ID {}</p>'.format(id))