from django.conf.urls import url,include
from django.contrib import admin
from django.urls import path
from .import views

app_name='user_login'

urlpatterns = [
    path('signup/',views.signup_view,name='signup_view'),
    path('login/',views.login_view,name='login_view'),
    path('logout/',views.logout_view,name='logout_view'),
]