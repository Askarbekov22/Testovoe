from django.urls import path
from .views import RegisterView,VerifyEmail, LoginAPIView,MessageView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginAPIView.as_view(), name="login"),
    path('email-verify/', VerifyEmail.as_view(), name="email-verify"),
    path('send-message/',MessageView.as_view(),name = 'send-message'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
