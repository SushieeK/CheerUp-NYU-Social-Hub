from django.db import models
from location.models import Location
from django.contrib.auth.models import User
from tags.models import Tag
from .constants import STATUS_CHOICES, PENDING

# Create your models here.


class Event(models.Model):
    event_name = models.CharField(max_length=200)
    event_location = models.ForeignKey(Location, on_delete=models.CASCADE, default=261)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    capacity = models.IntegerField()
    is_active = models.BooleanField(default=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.event_name


class EventJoin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING)

    class Meta:
        unique_together = ("user", "event")

    def __str__(self):
        return f"{self.user.username} - {self.event.event_name} - {self.get_status_display()}"
