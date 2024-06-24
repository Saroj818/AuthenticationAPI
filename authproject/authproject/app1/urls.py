"""Urls definition for the app"""

from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt import views as jwt_views

from . import views

urlpatterns = [
    path('basic/auth', views.BasicAuthView.as_view(), name='basic_auth' ),
    path('token/auth', obtain_auth_token, name='token_auth'),
    path('token/example', views.TokenExampleView.as_view(), name='token_example'),
    path('jwt/token/',
         jwt_views.TokenObtainPairView.as_view(),
         name ='token_obtain_pair'),
    path('jwt/refresh/',
         jwt_views.TokenRefreshView.as_view(),
         name ='token_refresh'),
    path('jwt/example', views.JwtExampleView.as_view(), name='jwt_example'),
    path('country', views.country, name='country')

]
