from django.urls import path
from .views import RegisterView, UserListView, UserDeleteView

urlpatterns = [
    path("", RegisterView.as_view(), name="register"),
    path("list/", UserListView.as_view(), name="user-list"),
    path("delete/<int:pk>/", UserDeleteView.as_view(), name="user-delete"),
]
