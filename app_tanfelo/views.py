from django.shortcuts import render

from .models import Tanar, Tantargy
# Create your views here.

def kmklista(request):
    template='kmklista.html'
    osszes_tanar = Tanar.objects.all()
    context = {
        'tanarok': osszes_tanar,
        }
    return render(request, template, context)
