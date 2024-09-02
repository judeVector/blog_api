from django.urls import path

from .views import *

urlpatterns = [
    path("auth/signup/", SignUpView.as_view(), name="signup"),
    path("auth/signin/", LoginView.as_view(), name="signin"),
    path("auth/regenerate/", RegenerateTokenView.as_view(), name="regenerate"),
]
