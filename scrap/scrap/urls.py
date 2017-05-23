from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from scr import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^scr/', include('scr.urls')),
]
