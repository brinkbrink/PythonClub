from django.db import models
from django.forms import DateField
from django.contrib.auth.models import User

# Create your models here.
# Meeting which will have fields for meeting title, meeting date, meeting time, location, Agenda
# Meeting Minutes which will have fields for meeting id (a foreign key), attendance (a many to many field with User), Minutes text
# Resource which will have fields for resource name, resource type, URL, date entered, user id (foreign key with User), and description
# Event which will have fields for event title, location, date, time, description and the user id of the member that posted it

class Meeting(models.Model):
    title=models.CharField(max_length=250)
    # user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date=models.DateField()
    time=models.TimeField()
    location=models.CharField(max_length=250)
    agenda=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table='meeting'

class MeetingMin(models.Model):
    meetid=models.ForeignKey(Meeting, on_delete=models.DO_NOTHING)
    userid=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    minutes=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.minutes

    class Meta:
        db_table='meetingmin'

class Resource(models.Model):
    name=models.CharField(max_length=250)
    type=models.CharField(max_length=250)
    url=models.URLField()
    dateentered=DateField()
    userid=models.ForeignKey(User, on_delete=models.CASCADE)
    description=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table='resource'

class Event(models.Model):
    title=models.CharField(max_length=250)
    location=models.CharField(max_length=250)
    date=models.DateField()
    time=models.TimeField()
    evdescription=models.TextField(null=True, blank=True)
    userid=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table='event'