from django.shortcuts import render


def home(request):
    return render(request, 'webpages/base.html')

def logado(request):
    return render(request, 'webpages/testando.html')

