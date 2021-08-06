"""auth_google URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from userProfile import views
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='home'),
    path('admin/', admin.site.urls),
    re_path(r'^api/userProfiles/$', views.userProfile_list),
    re_path(r'^api/userProfiles/([0-9])$', views.userProfiles_detail),
    path('accounts/', include('allauth.urls')),
    path(r'^$/', views.index, name='default'),
]
