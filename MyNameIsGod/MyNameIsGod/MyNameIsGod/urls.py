
from django.contrib import admin
from django.urls import path,include
from membersapi import views




urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',include('membersapi.urls')),
    
]
