from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'webpages-home'),
    path('login/', views.login, name = 'webpages-login'),
    path('registrar/', views.login, name = 'webpages-registrar'),

]