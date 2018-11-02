from django.urls import path

from voos import views

urlpatterns = [
    path('', views.ListarVoo.as_view(), name='listar_voo'),
    path('novo', views.NovoVoo.as_view(), name='novo_voo'),
    path(
        'visualizar/<int:pk>',
        views.VisualizarVoo.as_view(),
        name='visualizar_voo'
    ),
    path('editar/<int:pk>', views.EditarVoo.as_view(), name='editar_voo'),
    path('apagar/<int:pk>', views.ApagarVoo.as_view(), name='apagar_voo'),
]
