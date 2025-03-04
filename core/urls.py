
from django.contrib import admin
from django.urls import path
from app_main import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', views.InitiView.as_view(), name='bazar'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
