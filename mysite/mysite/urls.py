from django.contrib import admin
from django.urls import path, include

# mapping the addresses with corresponding application

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),
    path('polls/', include('polls.urls'))
]

# mapper