from django.shortcuts import render

from django.contrib.auth.models import User
from events.models import EventCategory, Event

def dashboard(request):
    user = User.objects.count()
    event_ctg = EventCategory.objects.count()
    event = Event.objects.count()
    complete_event = Event.objects.filter(status='completed').count()
    context = {
        'user': user,
        'event_ctg': event_ctg,
        'event': event,
        'complete_event': complete_event
    }
    return render(request, 'dashboard.html', context)