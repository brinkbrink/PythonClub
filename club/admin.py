from django.contrib import admin
from .models import Meeting, MeetingMin, Resource, Event
# Register your models here.
admin.site.register(Meeting)
admin.site.register(MeetingMin)
admin.site.register(Resource)
admin.site.register(Event)