"""
URL configuration for token_project project.

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
from django.contrib import admin
from django.urls import path
# from rest_framework.authtoken.views import obtain_auth_token
# from api.auth import CustomAuthToken
from api.views import ChairAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/',ChairAPI.as_view()),
    # path('gettoken/',obtain_auth_token),# this ulr use for end point api to get token with username and password
    # path('gettoken/',CustomAuthToken.as_view()),# this url fuse for and point api to get token with username and password with more inforamtion 
]
