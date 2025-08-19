from django.urls import path
from .views import UserListView, UserDeleteView

urlpatterns = [
    path("", UserListView.as_view(), name="user-list"),
    path("<int:pk>/", UserDeleteView.as_view(), name="user-delete"),
]
