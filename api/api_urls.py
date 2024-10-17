
from django.urls import path, include, re_path
from api.views import login



urlpatterns = [
    path("login/", login.LoginView.as_view()),

]
