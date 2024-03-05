from django.db import models
import uuid
from .grouping import *
# from . import perks

# The data models for the Wikitech student registration DBMS, this data models holds info concerning the members in the club
#members
class Membership(models.Model):
    member_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    other_names = models.CharField(max_length=255, blank=True)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=255)
    college = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    graduation_year = models.IntegerField(null=True, blank=True)
    company = models.CharField(max_length=255, blank=True)
    job_title = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=255)
    date_joined = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    # assigned_group = models.ForeignKey(FanGroup, null=True, on_delete=models.CASCADE)
    # assigned_id = models.UUIDField(default=uuid.uuid4, editable=False)


#projects
class ProjectInfo(models.Model):
    project_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=255)
    date_started = models.DateField()

#staff
class Staff(models.Model):
    staff_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    other_names = models.CharField(max_length=255, blank=True)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=255)
    college = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    date_joined = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

# events
class Event(models.Model):
    event_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    venue = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

class EventAttendance(models.Model):
    attendance_id = models.IntegerField(primary_key=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    member = models.ForeignKey(Membership, on_delete=models.CASCADE)
    date_attended = models.DateField(auto_now_add=True)

# cashbook
class Cashbook(models.Model):
    transaction_id = models.IntegerField(primary_key=True)
    date = models.DateField()
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=255)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

#make wiki tech fan group a many to one model
class FanGroup(models.Model):
    group_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    date_created = models.DateField(auto_now_add=True)
    members = models.ManyToManyField('Membership', 'ProjectInfo', 'Staff')

