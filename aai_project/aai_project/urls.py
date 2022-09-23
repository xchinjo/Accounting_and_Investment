from django.contrib import admin
from django.urls import path
from aaiapp.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home)
]
