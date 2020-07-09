from django.urls import path

from . import views
urlpatterns = [
    path('', views.index, name = 'index'),
    path('lista', views.lista, name = 'lista'),
    path('añadir', views.añadir, name= 'añadir'),
    path('editar/<int:id>/', views.editar, name= 'editar'),
    #path('eliminar/<int:id>/', views.eliminar, name= 'eliminar'),

]
