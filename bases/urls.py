from django.urls import path
from django.contrib.auth import views as auth_view
from bases.views import Home

urlpatterns=[
    path('',Home.as_view(),name='home'),
    path('login/', auth_view.LoginView.as_view(template_name='bases/login.html'), name= 'login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='bases/login.html'), name= 'logout')
]