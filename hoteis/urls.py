from django.urls import path

from hoteis import views

urlpatterns = [
    path('', views.ListarHotel.as_view(), name='listar_hotel'),
    path('novo', views.NovoHotel.as_view(), name='novo_hotel'),
    path(
        'visualizar/<int:pk>',
        views.VisualizarHotel.as_view(),
        name='visualizar_hotel'
    ),
    path(
        'editar/<int:pk>',
        views.EditarHotel.as_view(),
        name='editar_hotel'
    ),
    path(
        'apagar/<int:pk>',
        views.ApagarHotel.as_view(),
        name='apagar_hotel'
    ),
]
