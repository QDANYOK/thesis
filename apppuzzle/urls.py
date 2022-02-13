from django.template.defaulttags import url
from django.urls import path

from .views import *
app_name='pu'
urlpatterns = [
    path('', image_upload_view, name='upload'),
    path('game/', PuzzleView.as_view(), name='puzzle'),


]
