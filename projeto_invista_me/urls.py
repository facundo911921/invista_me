from django.contrib import admin
from django.urls import path
from invista_me import views
from usuarios import views as usuarios_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.investimentos, name="investimentos"),
    path("conta/", usuarios_views.novo_usuario, name="novo_usuario"),
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', auth_views.LoginView.as_view(template_name='usuarios/logout.html'), name='logout'),
    path("contato_html/", views.contato_html, name="contato_html"),
    path("novo_investimento/", views.criar, name="novo_investimento"),
    path("excluir_investimento/<int:id_investimento>", views.excluir, name="excluir"),
    path("novo_investimento/<int:id_investimento>", views.editar, name="editar"),
    path("/<int:id_investimento>", views.detalhe, name="detalhe")
]
