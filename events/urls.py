from django.urls import path

from .views import (
    EventCategoryListView,
    EventCategoryCreateView,
)

urlpatterns = [
    path('event-category-list/', EventCategoryListView.as_view(), name='event-category-list'),
    path('create-event-category/', EventCategoryCreateView.as_view(), name='create-event-category'),
]