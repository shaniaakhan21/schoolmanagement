from django.urls import path
#url mapping for user login app
from . import views  # (as user_views not in used here) #importing user/views.py as user_views
from django.contrib.auth import views as auth_views




urlpatterns = [
    path('register/', views.register, name = 'register'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html') , name = 'login'), #built-in views for login that django gave to handle logic
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html') , name = 'logout'),

]
