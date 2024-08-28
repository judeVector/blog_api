from django.urls import path

from .views import *

urlpatterns = [
    path("auth/signup/", SignUpView.as_view(), name="signup"),
]
