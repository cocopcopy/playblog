from django import template
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


register = template.library()


@register.simple_tag(takes_context=True)
def paginate(context, page_list, per_num):
	left_num = 3
	right_num = 3

	paginator = Paginator(page_list, per_num)
	wanted_page = context['request'].GET.get('page')

	try:
		wanted_list = paginator.page(wanted_page)
		context['current_page'] = wanted_page
		pages = range(max(1, wanted_page - left_num), min(paginator.num_pages + 1, wanted_page + right_num))
	except PageNotAnInteger:
		wanted_list = paginator.page(1)
		context['current_page'] = 1
		# in this case, we just need display the right page info
		pages = range(1, min(1 + left_num, paginator.num_pages + 1))
	except EmptyPage:
		# in this case, we consider that user request page with a null value
		# then we return the last page to him
		wanted_list = paginator.page(paginator.num_pages)
		context['current_page'] = paginator.num_pages
		pages = range(max(1, paginator.num_pages - right_num), paginator.num_pages)

	# what we need besides current_pge, also: article_list
	# last_page, first_page, and the page list: pages
	context['pages'] = pages
	context['first_page'] = 1
	context['last_page'] = paginator.num_pages
	context['article_list'] = wanted_list

	try:
		context['first_page'] = page[0]
		context['last_page'] = page[-1] + 1
	except IndexError:
		context['first_page'] = 1
		context['last_page'] = 2

	return ''
