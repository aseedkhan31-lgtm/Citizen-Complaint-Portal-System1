from django.urls import path
from . import views
urlpatterns = [
    path('', views.user_dashboard_view, name='user_dashboard_view'),
    path('admin_dashboard/', views.admin_dashboard_view, name='admin_dashboard_view'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register_view, name='register_view'),
]