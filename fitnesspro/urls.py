#urls.py

from django.contrib import admin
from django.urls import path, include
#from myapp import views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dietwork/', include('dietwork.urls')),
    path('admin/', admin.site.urls),
    path('tracker/', include('myapp.urls')),
    path('accounts/', include('accounts.urls')),
]
