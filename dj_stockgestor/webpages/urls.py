from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'webpages-home'),
    path('logado/', views.logado, name = 'webpages-logado'),
]