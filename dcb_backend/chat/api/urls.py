from django.urls import path
from . import views

urlpatterns = [
    path('ask', views.ChatAsk.as_view()),
    path('history', views.ChatHistory.as_view()),
]
