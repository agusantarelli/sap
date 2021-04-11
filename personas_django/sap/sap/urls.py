from django.contrib import admin
from django.urls import path
from webapp.views import bienvenido,personas,about
from personas.views import detallePersona,nuevaPersona,editarPersona,eliminarPersona,domicilios,editarDomicilio,eliminarDomicilio,nuevoDomicilio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',bienvenido,name='index'),
    path('listado_personas',personas,name='listperson'),
    path('detalle_persona/<int:id>',detallePersona),
    path('nueva_persona',nuevaPersona, name = 'nueva'),
    path('editar_persona/<int:id>',editarPersona),
    path('eliminar_persona/<int:id>',eliminarPersona),
    path('listado_domicilio',domicilios,name = 'listado'),
    path('about',about),
    path('editar_domicilio/<int:id>',editarDomicilio),
    path('eliminar_domicilio/<int:id>',eliminarDomicilio),
    path('nuevo_domicilio',nuevoDomicilio,name='nuevodomi'),
]
