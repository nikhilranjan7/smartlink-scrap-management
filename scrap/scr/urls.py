from django.conf.urls import url
from scr import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.add, name='add'),
    #url(r'^quotes/$', views.quotes, name='quotes')
]
