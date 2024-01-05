
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static

from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home , name ='home'),
    path('', include('authentication.urls')),
    path('', include('profil.urls')),
    path('', include('product.urls')),
    path('brand/<str:carname>/', views.home, name='card' ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
