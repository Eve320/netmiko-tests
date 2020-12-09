from django.urls import path

from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('device/<int:device_id>', views.get_config, name="device"),
    
]