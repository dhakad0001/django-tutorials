
from django.urls import path 
from polls.views import index

urlpatterns = [
    path('', index)
]