from django.urls import path 
from . import views

urlpatterns = [
#    path('', 'views.show'),
path('', views.show)
]
