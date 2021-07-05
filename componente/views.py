from django.shortcuts import render

# Create your views here.

def _bienvenida(request):
    return render(request, "index.html")