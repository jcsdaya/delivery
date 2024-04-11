from django.urls import path
from. import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('dispatchhome/',views.dispatchhome,name="dispatchhome"),
  path('dispatchcomplete/',views.dispatchcomplete,name="dispatchcomplete"),
  path('dispatchupdate/<str:pk>/',views.dispatchupdate,name="dispatchupdate"),
  path('dispatchdecline/<str:pk>/',views.dispatchdecline,name="dispatchdecline"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)