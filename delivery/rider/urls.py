from django.urls import path
from. import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('riderhome/',views.riderhome,name="riderhome"),
  path('rideredit/<str:pk>/',views.rideredit,name="rideredit"),
  path('riderdelete/<str:pk>/',views.riderdelete,name="riderdelete"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)