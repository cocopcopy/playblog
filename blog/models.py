from django.db import models


# Create your models here.
class Article(models.Model):
	STATUS_CHOICES = (
		('d', 'Draft'),
		('p', 'Published')
		)

	title = models.CharField('Title', max_length=70)
	body = models.TextField('Article')
	# setting param: auto_now_add as True, then date will automaticlly created when added
	created_time = models.DateTimeField('Created_Date', auto_now_add=True)
	last_modified_time = models.DateTimeField('Modified_Time', auto_now=True)
	status = models.CharField('Status', max_length=1, choices=STATUS_CHOICES)
	abstract = models.CharField('Abstract', max_length=54, blank=True, null=True, help_text='可选，如若为空将摘取正文的前54个字符')

	views = models.PositiveIntegerField('View_Num', default=0)
	likes = models.PositiveIntegerField('Like_Num', default=0)
	topped = models.BooleanField('Topped', default=False)

	# if category is deleted, then set the variable: category with null
	category = models.ForeignKey('Category', verbose_name='Cite', null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-last_modified_time']


class Category(models.Model):
	name = models.CharField('Cite_Name', max_length=20)
	created_time = models.DateTimeField('Created_Time', auto_now_add=True)
	last_modified_time = models.DateTimeField('Modified_Time', auto_now=True)

	def __str__(self):
		return self.name
