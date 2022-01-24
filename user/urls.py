from django.urls import path

from . import views
from .views import CreateView, LoginView

urlpatterns = [
    path('', views.index),
    path('create', CreateView.as_view()),
    path('login', LoginView.as_view()),
]