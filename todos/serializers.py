from rest_framework import serializers
from todos.models import Notes, Reminder

class NotesSerializers(serializers.ModelSerializer):

    class Meta:
        model = Notes
        fields = "__all__"

class ReminderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reminder
        fields = "__all__"


