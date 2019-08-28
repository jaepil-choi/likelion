from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:blog_id>', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),

    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]


