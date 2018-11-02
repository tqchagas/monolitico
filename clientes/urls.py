from django.urls import path

from clientes import views

urlpatterns = [
    path('', views.ListarCliente.as_view(), name='listar_cliente'),
    path('novo', views.NovoCliente.as_view(), name='novo_cliente'),
    path(
        'visualizar/<int:pk>',
        views.VisualizarCliente.as_view(),
        name='visualizar_cliente'
    ),
    path(
        'editar/<int:pk>',
        views.EditarCliente.as_view(),
        name='editar_cliente'
    ),
    path(
        'apagar/<int:pk>',
        views.ApagarCliente.as_view(),
        name='apagar_cliente'
    ),
]
