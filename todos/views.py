from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from todos.models import Notes, Reminder
from todos.serializers import (NotesSerializers, 
                                ReminderSerializer
                                )

def index(request):
    return HttpResponse("Here is a Todo App!!")

class NotesListAPIView(generics.ListAPIView):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializers

class ReminderListAPIView(generics.ListAPIView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer


