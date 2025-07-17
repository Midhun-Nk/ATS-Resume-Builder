from django.urls import path
from accounts.views import login_view,home_view,register_view,logout_view

urlpatterns = [
        path('login/',login_view, name='login'),
    path('home/',home_view, name='home'),
    path('register/',register_view, name='register'),
    path('logout/',logout_view, name='logout'),
    
]
