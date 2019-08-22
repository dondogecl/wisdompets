from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from .models import Pet

# Create your views here.
def home(request):
    #return HttpResponse('<p>Home view</p>')
    pets = Pet.objects.all()
    # render
    return render(request, 'home.html', {'pets' : pets}) #obj request, template a usar, diccionario con la data que usaremos
    

def pet_detail(request, id):
    #return HttpResponse('<p>Pet Detail view with the ID {}</p>'.format(id))
    try:
        pet = Pet.objects.get(id=id)
    except Pet.DoesNotExist:
        raise Http404('Pet not found')
    return render(request, 'pet_detail.html', {'pet': pet})