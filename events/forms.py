from django import forms

from .models import Event

class EventForm(forms.ModelForm):


    class Meta:
        model = Event
        fields = ['category', 'name', 'uid', 'description', 'scheduled_status', 'venue', 'agenda', 'start_date', 'end_date', 'location', 'points', 'maximum_attende', 'status', 'image', 'notification']
        widgets = {
            'start_date': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
        }