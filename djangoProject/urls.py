"""djangoProject URL Configuration

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
from typing import Union

from django.urls import URLResolver
from django.contrib import admin
from django.urls import path, include

urlpatterns: list[Union[URLResolver, URLResolver]] = [
    path('polls/', include('polls.urls')),
    path('handwriting/', include('wikipedia_converter.urls')),
    path('', include('wikipedia_converter.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include("django.contrib.auth.urls"))
]
