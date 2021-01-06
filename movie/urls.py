from django.contrib import admin
from django.conf import settings
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
    path('conta/', include('usuarios.urls', namespace='conta')),
    path('filme/', include('filmes.urls', namespace='filme')),    
    path('perfil/', include('perfil.urls', namespace='perfil'))
]
