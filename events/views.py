from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DetailView,
)

from .models import EventCategory, Event

# Event category list view
class EventCategoryListView(ListView):
    model = EventCategory
    template_name = 'events/event_category.html'
    context_object_name = 'event_category'


class EventCategoryCreateView(CreateView):
    model = EventCategory
    fields = ['name', 'code', 'image', 'priority', 'status']
    template_name = 'events/create_event_category.html'

    def form_valid(self, form):
        form.instance.created_user = self.request.user
        form.instance.updated_user = self.request.user
        return super().form_valid(form)


class EventCategoryUpdateView(UpdateView):
    model = EventCategory
    fields = ['name', 'code', 'image', 'priority', 'status']
    template_name = 'events/edit_event_category.html'


class EventCreateView(CreateView):
    model = Event
    fields = ['category', 'name', 'uid', 'description', 'scheduled_status', 'venue', 'agenda', 'start_date', 'end_date', 'location', 'points', 'maximum_attende', 'status']
    template_name = 'events/create_event.html'

    def form_valid(self, form):
        form.instance.created_user = self.request.user
        form.instance.updated_user = self.request.user
        return super().form_valid(form)


class EventListView(ListView):
    model = Event
    template_name = 'events/event_list.html'
    context_object_name = 'events'


class EventUpdateView(UpdateView):
    model = Event
    fields = ['category', 'name', 'uid', 'description', 'scheduled_status', 'venue', 'agenda', 'start_date', 'end_date', 'points', 'maximum_attende', 'status']
    template_name = 'events/edit_event.html'


class EventDetailView(DetailView):
    model = Event
    template_name = 'events/event_detail.html'
    context_object_name = 'event'

