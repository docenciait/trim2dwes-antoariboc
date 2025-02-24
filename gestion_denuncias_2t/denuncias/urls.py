from django.urls import path
from . import views
urlpatterns = [
    path('denuncias/', views.lista_denuncias, name='denuncias.lista_denuncias'),
    path('denuncias/crear/', views.crear_denuncia, name='denuncias.crear_denuncia'),
    path('denuncias/editar/<int:id>/', views.editar_denuncia, name='denuncias.editar_denuncia'),
    path('denuncias/eliminar/<int:id>/', views.eliminar_denuncia, name='denuncias.eliminar_denuncia'),
]