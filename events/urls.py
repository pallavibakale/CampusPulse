from django.urls import path
from events.views.categories import CategoryCreateView, CategoryListView, CategoryDetailView

from events.views.events import EventCreateView, EventDeleteView, EventListView, EventDetailView, EventUpdateView, add_students_to_event

urlpatterns = [
    # Student URLs
    path('create/', EventCreateView.as_view(), name='event-create'),
    path('category/', CategoryListView.as_view(), name='category-list'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('category/create/', CategoryCreateView.as_view(), name='category-create'),
    path('update/<int:pk>/', EventUpdateView.as_view(), name='event-update'),
    path('delete/<int:pk>/', EventDeleteView.as_view(), name='event-delete'),
    path('addStudents/<int:event_id>/', add_students_to_event, name='event-add-students'),
    path('', EventListView.as_view(), name='event-list'),
    path('<int:pk>/', EventDetailView.as_view(), name='event-detail'),
]
