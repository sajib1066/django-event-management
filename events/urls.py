from django.urls import path

from .views import (
    EventCategoryListView,
    EventCategoryCreateView,
    EventCategoryUpdateView,
    EventCreateView,
    EventListView,
    EventUpdateView,
    EventDetailView,
    AddEventMemberCreateView,
    JoinEventListView,
    RemoveEventMemberDeleteView,
    EventUserWishListView,
    AddEventUserWishListCreateView,
    RemoveEventUserWishDeleteView,
    UpdateEventStatusView,
    CompleteEventList,
    AbsenseUserList,
)

urlpatterns = [
    path('category-list/', EventCategoryListView.as_view(), name='event-category-list'),
    path('create-category/', EventCategoryCreateView.as_view(), name='create-event-category'),
    path('category/<int:pk>/edit/', EventCategoryUpdateView.as_view(), name='edit-event-category'),
    path('event-create/', EventCreateView.as_view(), name='event-create'),
    path('event-list/', EventListView.as_view(), name='event-list'),
    path('event/<int:pk>/edit/', EventUpdateView.as_view(), name='event-edit'),
    path('detail/<int:pk>', EventDetailView.as_view(), name='event-detail'),
    path('add-event-member/', AddEventMemberCreateView.as_view(), name='add-event-member'),
    path('join-event-list/', JoinEventListView.as_view(), name='join-event-list'),
    path('event-member/<int:pk>/remove/', RemoveEventMemberDeleteView.as_view(), name='remove-event-member'),
    path('event-wish-list/', EventUserWishListView.as_view(), name='event-wish-list'),
    path('add-event-wish-user/', AddEventUserWishListCreateView.as_view(), name='add-event-wish-user'),
    path('event-user-wish/<int:pk>/remove/', RemoveEventUserWishDeleteView.as_view(), name='remove-event-user-wish'),
    path('update-status/<int:pk>/event/', UpdateEventStatusView.as_view(), name='update-event-status'),
    path('complete-event/', CompleteEventList.as_view(), name='complete-event'),
    path('absense-user/', AbsenseUserList.as_view(), name='absense-user'),
]