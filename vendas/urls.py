from django.urls import path

from vendas import views

urlpatterns = [
    path('', views.ListarVenda.as_view(), name='listar_venda'),
    path('novo', views.NovaVenda.as_view(), name='novo_venda'),
    path(
        'visualizar/<int:pk>',
        views.VisualizarVenda.as_view(),
        name='visualizar_venda'
    ),
    path(
        'apagar/<int:pk>',
        views.ApagarVenda.as_view(),
        name='apagar_venda'
    ),
    path(
        'comissoes',
        views.RelatorioVendas.as_view(),
        name='comissoes'
    )
]
