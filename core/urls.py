
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
    path("contatc/", views.ContactViews.as_view(), name='contact'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)