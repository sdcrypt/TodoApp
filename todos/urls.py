from django.urls import path
from todos import views

urlpatterns = [
    path('', views.index, name='index'),
    path('notes/', views.NotesListAPIView.as_view(), name='notes-list'),
    path('reminders/', views.ReminderListAPIView.as_view(), name='reminders-list'),
]