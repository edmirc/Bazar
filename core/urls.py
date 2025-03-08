
from django.contrib import admin
from django.urls import path
from app_main import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.InitiView.as_view(), name='bazar'),
    path('detail/<int:pk>/', views.ProductDetailView.as_view(), name='detail'),
    path('category/<int:pk>', views.CategoryView.as_view(), name='category'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
