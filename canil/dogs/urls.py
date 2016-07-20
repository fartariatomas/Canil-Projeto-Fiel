from django.conf.urls import url
from . import views
from django.contrib import admin

app_name = 'dogs'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^admin/', admin.site.urls),
    url(r'^add/$', views.PhotoCreate.as_view(), name='photo-add'),
]
