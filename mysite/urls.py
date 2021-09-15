
from django.contrib import admin
from django.urls import path, include
from blog import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('', views.post_list, name = 'post_list'),
    path('post/<int:pk>/', views.post_detail, name = 'post_detail'),
    path('post/new', views.new_post, name = 'new_post' ),
    path('post/<int:pk>/edit', views.post_edit, name = 'post_edit'),


]
