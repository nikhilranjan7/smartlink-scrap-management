from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from scr import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^scr/', include('scr.urls')),
    url(r'^quote/$', views.quotes, name='quota'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
