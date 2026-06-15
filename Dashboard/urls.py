from django.urls import path
from . import views
urlpatterns = [
    path('', views.user_dashboard_view, name='user_dashboard_view'),
    path('admin_dashboard.html', views.admin_dashboard_view, name='admin_dashboard_view'),
    path('login.html', views.login_view, name='login_view'),
    path('register.html', views.register_view, name='register_view'),
]