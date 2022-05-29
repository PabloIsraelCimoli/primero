from multiprocessing import context
from django.shortcuts import render
from .models import Deporte

def home(request):
    deportes=Deporte.objects.all()
    context={'deporte': deporte, 'categoria':categoria}

    return render(request, 'appcimoli/home.html', context)
# Create your views here.
