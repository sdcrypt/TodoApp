from django.urls import path
from todos import views

urlpatterns = [
    path('', views.index, name='index'),
]