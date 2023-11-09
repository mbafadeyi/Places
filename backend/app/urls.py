from django.urls import path
from . import views

urlpatterns = [
    path("properties/", views.PropertyListCreateView.as_view()),
    path("properties/<int:pk>/", views.PropertyRetrieveUpdateDestroyView.as_view()),
    path("booking/", views.BookingListCreateView.as_view()),
    path("booking/<int:pk>/", views.BookingRetrieveUpdateDestroyView.as_view()),
]
