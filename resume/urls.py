from django.urls import path
from .views import create_resume
urlpatterns = [
    path('createnew',create_resume, name='create')
]
