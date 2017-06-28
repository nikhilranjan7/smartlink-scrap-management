from django.conf.urls import url
from scr import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^add/$', views.add, name='add'),
	url(r'^quote/$', views.quotes, name='quota'),
    url(r'^success/$', views.excel, name='exa'),
    url(r'^q/$', views.exce, name='exe'),
    url(r'^chat/$', views.chat, name='chat'),
    url(r'^trxn/$', views.trxn, name='trxn'),
    url(r'^trx/$', views.exc, name='trx'),
]
