from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'webpages/bases_1.html')

def login(request):
    return render(request, '')

def registrar(request):
    return render(request, '')

