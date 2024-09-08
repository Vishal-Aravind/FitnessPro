#dietwork/urls.py

from django.urls import path, include
from . import views

urlpatterns = [
    path('diet/',views.diet, name='diet'),
    path('workout/',views.workout, name='workout'),

]
