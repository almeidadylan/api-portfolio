from django.urls import path

from users.views import ListCreateUserView

urlpatterns = [
    path('users/', ListCreateUserView.as_view())
]