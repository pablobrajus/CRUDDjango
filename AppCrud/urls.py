from django.urls import path
from  AppCrud import views
from .views import eliminar, eliminar_producto

urlpatterns = [
        path('',views.inicio,name="inicio"),
        path('modificar',views.modificar,name="modificar"),
        path('eliminar',views.eliminar,name="eliminar"),
        path('eliminar_producto/<int:producto_id>/',eliminar_producto, name='eliminar_producto'),
        path('crear_producto',views.crear_producto,name='crear_producto'),
        path('modificar_producto/<int:producto_id>/',views.modificar_producto,name='modificar_producto'),
        path('filtrar_productos',views.filtrar_productos,name='filtrar_productos')
        
    ]
