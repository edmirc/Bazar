
from django.contrib import admin
from django.urls import path
from app_main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', views.InitiView.as_view(), name='bazar'),
]
