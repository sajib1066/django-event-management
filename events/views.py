from django.views.generic import ListView

from .models import EventCategory


class EventCategoryListView(ListView):
    model = EventCategory
    template_name = 'events/event_category.html'
    context_object_name = 'event_category'
