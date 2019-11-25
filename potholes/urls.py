from django.urls import path
from . import views

urlpatterns = [
    path('', views.parseJson, name='parse_json'),
]
