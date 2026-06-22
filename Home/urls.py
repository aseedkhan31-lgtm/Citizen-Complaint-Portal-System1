from django.urls import path
from . import views
urlpatterns = [
    path('', views.home_page_view, name='user_dashboard_view'),
    path('home_page/', views.home_page_view, name='home_page_view'),
    path('Dashboard/', views.dashboardApp, name='dashboardApp'),

    path('home_page/', views.admin_dashboard_view, name='admin_dashboard_view'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register_view, name='register_view'),
    
    
    path('update/<int:id>/', views.update_complaint, name='update_complaint'),
    path('logout/', views.logout_view, name='logout'),
    
]