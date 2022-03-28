from django.urls import path, include
from . import views

urlpatterns = [
    # DRF 사용하는 url
    path('write/', views.ReviewView.as_view()),
    path('', views.ReviewView.as_view()),
    path('<int:id>/', views.ReviewView.as_view()),
    path('edit/', views.ReviewView.as_view()),
    path('delete/', views.ReviewView.as_view())
]