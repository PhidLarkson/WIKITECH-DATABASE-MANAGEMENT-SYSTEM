from django import forms
from .models import Membership, ProjectInfo, Staff, Event, EventAttendance,FanGroup

class MembershipForm(forms.ModelForm):    
    class Meta:
        model = Membership
        fields = ('first_name', 'last_name', 'other_names', 'email', 'role', 'college', 'department', 'graduation_year', 'company', 'job_title', 'status')  

class ProjectInfoForm(forms.ModelForm):
    class Meta:
        model = ProjectInfo
        fields = ('name', 'description', 'status', 'date_started')

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ('first_name', 'last_name', 'other_names', 'email', 'role', 'college', 'department')

class EventForm(forms.ModelForm):     
    class Meta:
        model = Event
        fields = ('name', 'description', 'date', 'time', 'venue', 'status')

class EventAttendanceForm(forms.ModelForm):
    class Meta:
        model = EventAttendance
        fields = ('event', 'member')           

class FanGroupForm(forms.ModelForm):
    class Meta:
        model = FanGroup
        fields = ('name', 'description')

