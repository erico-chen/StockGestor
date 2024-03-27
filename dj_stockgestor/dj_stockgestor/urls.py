from django.contrib import admin
from django.urls import path, include
from app_cad_produto import views

urlpatterns = [
    # Rota, view, nome
    #path('admin/', admin.site.urls),
    path('',views.cad_produto,name='cadastro_produto'),
    path('produtos/listagem_estoque/',views.produtos,name='listagem_estoque')
    #rota = 'produtos/cadastro/'
]
