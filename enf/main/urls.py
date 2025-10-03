from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name='index'),
    path('/<int:pk>/',views.post_detail,name='post_detail'),
    path('register/',views.register_view,name='register'),
    path('logout/',views.logout_view,name='logout'),
    path('login/',views.login_view,name='login')
]