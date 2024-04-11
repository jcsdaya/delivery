
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('rider.urls')),
    path('', include('dispatch.urls')),
]
