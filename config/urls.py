"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from blog.views import post_list, post_detail, post_add, post_delete, post_delete_confirm

urlpatterns = [
    path('admin/', admin.site.urls),
    # post-list라는 URL에 온 요청은
    # blog.views.post_list함수가 처리한다
    path('posts/', post_list, name='url-name-post-list'),
    path('posts/<int:pk>/', post_detail, name='url-name-post-detail'),
    path('posts/<int:pk>/delete/', post_delete, name='url-name-post-delete'),
    path('posts/<int:pk>/delete/confirm/', post_delete_confirm, name='url-name-post-delete-confirm'),
    path('posts/add/', post_add, name='url-name-post-add'),
]