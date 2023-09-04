from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('Api_Aprendiz/', include('Api_Aprendiz.urls')),
]
