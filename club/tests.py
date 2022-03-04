from django.test import TestCase
from django.contrib.auth.models import User
from .models import Meeting, MeetingMin, Resource, Event
import datetime
from .forms import MeetingForm

# Create your tests here.
class MeetingTest(TestCase):
    def setUp(self):
        self.title=Meeting(title='Orientation Meeting')
        self.date=Meeting(date=datetime.date(2022,1,1))
        self.time=Meeting(time=datetime.time(hour=20, minute=2, second=1))

    def test_titlestring(self):
        self.assertEqual(str(self.title), 'Orientation Meeting')

    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')


class ResourceTest(TestCase):
    def setUp(self):
        self.name=Resource(name='A Resource')
    
    def test_namestring(self):
        self.assertEqual(str(self.name), 'A Resource')

    def test_tablename(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')

class EventTest(TestCase):
    def setUp(self):
        self.title=Event(title='Fat Tuesday')

    def test_evtitlestring(self):
        self.assertEqual(str(self.title), 'Fat Tuesday')

    def test_tablename(self):
        self.assertEqual(str(Event._meta.db_table), 'event')

class MeetingMinTest(TestCase):
    def setUp(self):
        self.meetid=Meeting(title='meeting')
        self.userid=User(username='user2')
        self.meetingmin=MeetingMin(meetid=self.meetid, userid=self.userid, minutes='Minutes of this meeting')

    def test_minstring(self):
        self.assertEqual(str(self.meetingmin), 'Minutes of this meeting')

    def test_tablename(self):
        self.assertEqual(str(MeetingMin._meta.db_table), 'meetingmin')

class NewMeetingForm(TestCase):
    #valid form data
    def test_meetingform(self):
        data={
            'title':'meeting', 
            'date':'2022-03-02', 
            'time':'10:00:00', 
            'location':'clubhouse', 
            'agenda':'none'}
        form=MeetingForm(data)
        self.assertTrue(form.is_valid)