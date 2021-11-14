from django.db import models
from datetime import datetime

class Notes(models.Model):
    LABEL_CHOICES = (
        ("inspiration", "Inspiration"),
        ("personal", "Personal"),
        ("work", "Work"),
    )
    title = models.CharField(max_length=200)
    note = models.TextField()
    labels = models.CharField(max_length=50, choices=LABEL_CHOICES)
    images = models.ImageField(upload_to='images/%Y/%m/%d')
    author = models.CharField(max_length=200)

    def __str__(self):
        return "{}".format(self.title)

class Reminder(models.Model):
    title = models.CharField(max_length=200)
    note = models.TextField()
    reminder_time = models.DateTimeField()
    images = models.ImageField(upload_to='images/%Y/%m/%d')

    def __str__(self):
        return "{}".format(self.title)

