from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('handwriting/', include('wikipedia_converter.urls')),
    path('', include('wikipedia_converter.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/create-user', views.get_create_user, name="getCreateUser"),
    path('accounts/create-user-db', views.create_user, name="createUser"),
    path('admin/', admin.site.urls),
]
