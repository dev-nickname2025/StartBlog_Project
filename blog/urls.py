from django.urls import path
from django.contrib.auth import login, authenticate
from . import views

urlpatterns = [
    path('', views.register_form, name='register'),
    path('login/', views.login_form, name='login'),
    path('logout/', views.logout_form, name='logout'),
    path('profile/', views.profile, name='profile'),

    # Blog Post URLs
    path('blog/', views.post_list, name='post_list'),
    path('blog/create/', views.create_post, name='create_post'),   
    path('blog/update/<int:pk>/', views.update_post, name='update_post'),
    path('blog/delete/<int:pk>/', views.delete_post, name='delete_post'),
    path('blog/<int:pk>/', views.post_detail, name='post_detail'),
]