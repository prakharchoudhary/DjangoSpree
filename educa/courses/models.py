from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from .fields import OrderField

# Create your models here.

class Subject(models.Model):
	
	title = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200, unique=True)

	class Meta:
		ordering = ('title',)

	def __str__(self):
		return self.title

class Course(models.Model):

	owner = models.ForeignKey(User, 
		related_name='courses_created')
	subject = models.ForeignKey(Subject, 
		related_name='courses')
	title = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200, unique=True)
	overview = models.TextField()
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ('-created',)

	def __str__(self):
		return self.title

class Module(models.Model):

	course = models.ForeignKey(Course,
		related_name='modules')
	title = models.CharField(max_length=200)
	description = models.TextField(blank=True)
	order = OrderField(blank=True, for_fields=['course'])

	class Meta:
		ordering = ['order']

	def __str__(self):
		return '{}. {}'.format(self.order, self.title)

class Content(models.Model):
	"""
	- content_type : A ForeignKey field to the ContentType model
	- object_id : This is PositiveIntegerField to store the primary key of the related object
	- item : A GenericForeignKey field to the related object by combining the two previous fields
	"""

	module = models.ForeignKey(Module, 
		related_name='contents')
	content_type = models.ForeignKey(ContentType,
		limit_choices_to={'model__in': ('text',
			'video', 'image', 'file')})
	object_id = models.PositiveIntegerField()
	item = GenericForeignKey('content_type', 'object_id')
	order = OrderField(blank=True, for_fields=['module'])

	class Meta:
		ordering = ['order']

class ItemBase(models.Model):

	owner = models.ForeignKey(User,
		related_name='%(class)s_related')
	title = models.CharField(max_length=250)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True

	def __str__(self):
		return self.title

class Text(ItemBase):
	content = models.TextField()

class File(ItemBase):
	file = models.FileField(upload_to='files')

class Image(ItemBase):
	file = models.FileField(upload_to='images')

class Video(ItemBase):
	url = models.URLField()