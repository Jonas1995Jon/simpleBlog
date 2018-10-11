from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'article/(?P<articleID>\d)$', views.article_page, name='article_page'),
    url(r'^edit_page/(?P<articleID>\d)$', views.edit_page, name='edit_page'),
    url(r'^edit/action/$', views.edit_action, name='edit_action'),
]