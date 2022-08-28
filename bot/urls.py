from . import views
from django.urls import path
from .config import *

urlpatterns = [
    path('', views.index, name='index'),
]

for url in urlsTelegram:
    urlpatterns.append(path('telegram/'+url, views.telegram, name='telegram'+url))
