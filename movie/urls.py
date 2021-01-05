from django.contrib import admin
from django.conf import settings
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls'), name='core'),
    path('conta/', include('usuarios.urls'), name='conta'),
    path('filme/', include('filmes.urls'), name='filme'),    
]
