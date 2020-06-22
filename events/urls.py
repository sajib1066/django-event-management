from django.urls import path

from .views import (
    EventCategoryListView,
    EventCategoryCreateView,
    EventCategoryUpdateView,
    EventCreateView,
    EventListView,
)

urlpatterns = [
    path('category-list/', EventCategoryListView.as_view(), name='event-category-list'),
    path('create-category/', EventCategoryCreateView.as_view(), name='create-event-category'),
    path('category/<int:pk>/edit/', EventCategoryUpdateView.as_view(), name='edit-event-category'),
    path('event-create/', EventCreateView.as_view(), name='event-create'),
    path('event-list/', EventListView.as_view(), name='event-list'),
]