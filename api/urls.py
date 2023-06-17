from django.urls import path
from . import views

urlpatterns = [
    path('get', views.getSong),
    path('upload-audio', views.upload_audio, name='upload_audio'),
]
