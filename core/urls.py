from django.urls import path

from core import views

urlpatterns = [
    path("", views.lista_produtos, name="lista_produtos"),
    path("criar/produto/", views.cria_produto, name="cria_produto")
]
