from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^article/(?P<article_id>\d+)$', views.ArticleView.as_view(), name='detail'),
	url(r'^category/(?P<cate_name>\d+)$', views.CategoryView.as_view(), name='cite')
]
