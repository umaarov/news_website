from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from news.views import news_list 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', news_list, name='news_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
