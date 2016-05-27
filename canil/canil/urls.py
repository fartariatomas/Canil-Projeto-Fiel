from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from canil import view


urlpatterns = [
    url(r'^$', view.homepage, name='homepage'),
    url(r'^admin/', admin.site.urls),
    url(r'^dogs/', include('dogs.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
