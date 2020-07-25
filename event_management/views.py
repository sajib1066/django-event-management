from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from events.models import EventCategory, Event
from .forms import LoginForm

@login_required(login_url='login')
def dashboard(request):
    user = User.objects.count()
    event_ctg = EventCategory.objects.count()
    event = Event.objects.count()
    complete_event = Event.objects.filter(status='completed').count()
    events = Event.objects.all()
    context = {
        'user': user,
        'event_ctg': event_ctg,
        'event': event,
        'complete_event': complete_event,
        'events': events
    }
    return render(request, 'dashboard.html', context)

def login_page(request):
    forms = LoginForm()
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('dashboard')
    context = {
        'form': forms
    }
    return render(request, 'login.html', context)

def logut_page(request):
    logout(request)
    return redirect('login')