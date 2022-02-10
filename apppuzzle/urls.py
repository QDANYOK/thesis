from django.template.defaulttags import url
from django.urls import path

from .views import *
app_name='pu'
urlpatterns = [
    path('', PuzzleView.as_view(), name='puzzle'),
    path('new/', post_new, name='new'),

]
