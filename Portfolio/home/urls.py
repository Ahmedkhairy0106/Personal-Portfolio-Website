from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='HOME'),
    path('about/', views.about, name='ABOUT'),
    path('contact/', views.contact, name='CONTACT'),
    path('projects/', views.projects, name='PROJECTS'),
    path('all_projects/', views.all_projects, name='ALL_PROJECTS'),
]