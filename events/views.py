from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
)
from django.urls import reverse_lazy
from django.shortcuts import render

from .models import (
    EventCategory,
    Event,
    JobCategory,
    EventJobCategoryLinking,
    EventMember,
    EventUserWishList,
    UserCoin,
)
from .forms import EventForm


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


class EventCategoryDeleteView(DeleteView):
    model =  EventCategory
    template_name = 'events/event_category_delete.html'
    success_url = reverse_lazy('event-category-list')


class EventCreateView(CreateView):
    model = Event
    fields = ['category', 'name', 'uid', 'description', 'scheduled_status', 'venue', 'agenda', 'start_date', 'end_date', 'location', 'points', 'maximum_attende', 'status', 'image', 'notification']
    template_name = 'events/create_event.html'

    def form_valid(self, form):
        form.instance.created_user = self.request.user
        form.instance.updated_user = self.request.user
        return super().form_valid(form)
    
    def get_form(self, form_class=EventForm):
        form = super(EventCreateView, self).get_form(form_class)
        form.fields['start_date'].widget.attrs.update({'class': 'datepicker'})
        form.fields['end_date'].widget.attrs.update({'class': 'datepicker'})
        return form


class EventListView(ListView):
    model = Event
    template_name = 'events/event_list.html'
    context_object_name = 'events'


class EventUpdateView(UpdateView):
    model = Event
    fields = ['category', 'name', 'uid', 'description', 'scheduled_status', 'venue', 'agenda', 'start_date', 'end_date', 'location', 'points', 'maximum_attende', 'status', 'image', 'notification']
    template_name = 'events/edit_event.html'


class EventDetailView(DetailView):
    model = Event
    template_name = 'events/event_detail.html'
    context_object_name = 'event'


class EventDeleteView(DeleteView):
    model = Event
    template_name = 'events/delete_event.html'
    success_url = reverse_lazy('event-list')


class AddEventMemberCreateView(CreateView):
    model = EventMember
    fields = ['event', 'user', 'attend_status', 'status']
    template_name = 'events/add_event_member.html'

    def form_valid(self, form):
        form.instance.created_user = self.request.user
        form.instance.updated_user = self.request.user
        return super().form_valid(form)


class JoinEventListView(ListView):
    model = EventMember
    template_name = 'events/joinevent_list.html'
    context_object_name = 'eventmember'


class RemoveEventMemberDeleteView(DeleteView):
    model = EventMember
    template_name = 'events/remove_event_member.html'
    success_url = reverse_lazy('join-event-list')


class EventUserWishListView(ListView):
    model = EventUserWishList
    template_name = 'events/event_user_wish_list.html'
    context_object_name = 'eventwish'


class AddEventUserWishListCreateView(CreateView):
    model = EventUserWishList
    fields = ['event', 'user', 'status']
    template_name = 'events/add_event_user_wish.html'

    def form_valid(self, form):
        form.instance.created_user = self.request.user
        form.instance.updated_user = self.request.user
        return super().form_valid(form)


class RemoveEventUserWishDeleteView(DeleteView):
    model = EventUserWishList
    template_name = 'events/remove_event_user_wish.html'
    success_url = reverse_lazy('event-wish-list')


class UpdateEventStatusView(UpdateView):
    model = Event
    fields = ['status']
    template_name = 'events/update_event_status.html'


class CompleteEventList(ListView):
    model = Event
    template_name = 'events/complete_event_list.html'
    context_object_name = 'events'

    def get_queryset(self):
        return Event.objects.filter(status='complete')


class AbsenseUserList(ListView):
    model = EventMember
    template_name = 'events/absense_user_list.html'
    context_object_name = 'absenseuser'

    def get_queryset(self):
        return EventMember.objects.filter(attend_status='absense')


class CompleteEventUserList(ListView):
    model = EventMember
    template_name = 'events/complete_event_user_list.html'
    context_object_name = 'completeuser'

    def get_queryset(self):
        return EventMember.objects.filter(attend_status='completed')


class CreateUserMark(CreateView):
    model = UserCoin
    fields = ['user', 'gain_type', 'gain_coin', 'status']
    template_name = 'events/create_user_mark.html'

    def form_valid(self, form):
        form.instance.created_user = self.request.user
        form.instance.updated_user = self.request.user
        return super().form_valid(form)


class UserMarkList(ListView):
    model = UserCoin
    template_name = 'events/user_mark_list.html'
    context_object_name = 'usermark'


def search_event_category(request):
    if request.method == 'POST':
       data = request.POST['search']
       event_category = EventCategory.objects.filter(name__icontains=data)
       context = {
           'event_category': event_category
       }
       return render(request, 'events/event_category.html', context)
    return render(request, 'events/event_category.html')


def search_event(request):
    if request.method == 'POST':
       data = request.POST['search']
       events = Event.objects.filter(name__icontains=data)
       context = {
           'events': events
       }
       return render(request, 'events/event_list.html', context)
    return render(request, 'events/event_list.html')