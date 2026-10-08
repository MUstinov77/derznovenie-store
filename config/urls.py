from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from site_app.views import favicon_ico, index, robots_txt, sitemap_xml

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path('robots.txt', robots_txt),
    path('sitemap.xml', sitemap_xml),
    path('favicon.ico', favicon_ico),
    path('', index, name='index'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
