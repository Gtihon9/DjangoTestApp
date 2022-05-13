from django.contrib import admin
from django.urls import path, include

from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accaounts/login/', views.LoginView.as_view(), name='login'),
    path('', include('blog.urls')),
]