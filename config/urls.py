"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from post.views import CategoryListCreateView, CategoryDetailView, TagListCreateView, TagDetailView, PostListCreateView, PostDetailView

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category-list'),
    path('categories/<slug:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('tags/', TagListCreateView.as_view(), name='tag-list'),
    path('tags/<slug:pk>/', TagDetailView.as_view(), name='tag-detail'),
    path('posts/', PostListCreateView.as_view(), name='post-list'),
    path('posts/<slug:pk>/', PostDetailView.as_view(), name='post-detail'),
]
