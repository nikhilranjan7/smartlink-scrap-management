from django.conf.urls import url
from scr import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
