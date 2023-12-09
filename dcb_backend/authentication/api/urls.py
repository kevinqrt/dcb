from django.urls import path, include
from dj_rest_auth.views import LoginView
from dj_rest_auth.jwt_auth import get_refresh_view


urlpatterns = [
    path('login/', LoginView.as_view()),
    path('refresh/', get_refresh_view().as_view(), name='token_refresh'),
]
