"""
URL configuration for arreinmuebles project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app.views import actualizar_usuario,actualizar_inmueble,eliminar_inmueble,registro_usuario,index,detalle_inmueble, cambiar_estado_solicitud,generar_solicitud_arriendo,crear_inmueble,solicitudes_arrendador,dashboard 
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from onlydepas import settings

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('registro/', registro_usuario, name='registro_usuario'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
    path('inmueble/<int:id>',detalle_inmueble , name='detalle'),
    
    path('inmuebles/<int:id>/generar-solicitud/', generar_solicitud_arriendo, name='generar_solicitud_arriendo'),
    
    path('inmueble/<int:id>/editar_inmueble/', actualizar_inmueble, name='editar_inmueble'),
    path('inmueble/<int:id>/eliminar_inmueble/', eliminar_inmueble, name='eliminar_inmueble'),
    
    path('crear_inmueble/', crear_inmueble, name='crear_inmueble'),
    path('solicitudes/', solicitudes_arrendador, name='solicitudes_arrendador'),
    
    path('dashboard/', dashboard, name='dashboard'),
    path('perfil/', actualizar_usuario, name='actualizar_usuario'),
    path('cambiar_estado_solicitud/<int:solicitud_id>/', cambiar_estado_solicitud, name='cambiar_estado_solicitud'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)