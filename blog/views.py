from django.shortcuts import render
from .models import Article, Category
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
import markdown2


# Create your views here.
class IndexView(ListView):
	template_name = 'blog/index.html'
	context_object_name = 'article_list'

	def get_queryset(self):
		article_list = Article.objects.filter(status='p')
		for article in article_list:
			article.body = markdown2.markdow(article.body,)
		return article_list

	def get_context_data(self, **kwargs):
		# get all cite
		kwargs['category_list'] = Category.objects.all().order_by('name')
		return super(IndexView, self).get_context_data(**kwargs)


class ArticleView(DetailView):
	template_name = 'blog/detail.html'
	model = Article
	context_object_name = 'article'

	pk_url_kwarg = 'article_id'

	def get_object(self):
		# use article_id get articl object
		obj = super(ArticleView, self).get_object()
		obj.body = markdown2.markdow(obj.body)
		return obj


class CategoryView(ListView):
	template_name = 'blog/index.html'
	context_object_name = 'article_list'

	def get_queryset(self):
		article_list = Article.objects.filter(self.kwargs['cate_name'], status='p')
		for article in article_list:
			article.body = markdown2.markdow(article.body,)
		return article_list

	def get_context_data(self, **kwargs):
		kwargs['category_list'] = Category.objects.all().order_by('name')
		return super(IndexView, self).get_context_data(**kwargs)
