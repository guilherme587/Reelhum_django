from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reelhum/', views.login, name='login'),
    path('reelhum/login', views.login, name='login'),
    path('reelhum/cadastro', views.cadastro, name='cadastro'),
    path('reelhum/logout', views.logout, name='logout'),
    path('reelhum/home/', views.home, name='home'),
    path('reelhum/home/vendas/', views.vendas, name='vendas'),
    path('reelhum/home/vendas/criar_venda/', views.criar_venda, name='criar_venda'),
    path('reelhum/home/vendas/editar_venda/<int:id>', views.editar_venda, name='editar_venda'),
    path('reelhum/home/vendas/deletar_venda/<int:id>', views.deletar_venda, name='deletar_venda'),
    path('reelhum/home/estoque/', views.estoque, name='estoque'),
    path('reelhum/home/estoque/criar_produto/', views.criar_produto, name='criar_produto'),
    path('reelhum/home/estoque/editar_produto/<int:id>', views.editar_produto, name='editar_produto'),
    path('reelhum/home/estoque/adicionar_produto/<int:id>', views.adicionar_produto, name='adicionar_produto'),
    path('reelhum/home/estoque/subtrair_produto/<int:id>', views.subtrair_produto, name='subtrair_produto'),
    path('reelhum/home/estoque/deletar_produto/<int:id>', views.deletar_produto, name='deletar_produto'),
    path('reelhum/home/estoque/custos_aquisicao', views.custos_aquisicao, name='custos_aquisicao'),
    path('reelhum/home/estoque/margem_lucro', views.margem_lucro, name='margem_lucro'),
]
