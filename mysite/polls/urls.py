
from django.urls import path 
from polls.views import *

urlpatterns = [
    path('showpolls/', show_polls)
]