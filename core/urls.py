from django.urls import path

from core import views

urlpatterns = [
#   READ
    path("", views.lista_produtos, name="lista_produtos"),
    path("compras/", views.lista_de_compras, name="lista_de_compras"),
    path("lista/marcas", views.lista_marcas, name="lista_marcas"),
#   CREATE
    path("criar/produto/", views.cria_produto, name="cria_produto"),
    path("criar/marca/", views.cria_marca, name="cria_marca"),
#   DELETE
    path("deletar/conf/produto/<id>", views.confirma_deleta_produto, name="confirma_deleta_produto"),
    path("deletar/produto/<id>", views.deleta_produto, name="deleta_produto"),
#   UPDATE
    path("comprar/<id>", views.comprar, name="compra_produto"),
    path("usar/<id>", views.usar, name="usa_produto"),
    path("editar/<id>", views.editar_produto, name="editar_produto"),
]
