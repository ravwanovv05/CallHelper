from django.urls import path

from users.views.users import RegistrationView

urlpatterns = [
    path('register', RegistrationView.as_view(), name='register'),
]