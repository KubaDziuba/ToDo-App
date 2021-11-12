from django.db import models


class Category(models.Model):
	cat_name = models.CharField('Category', max_length=30)

	def __str__(self):
		return self.cat_name


class Task(models.Model):
	category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE)
	name = models.CharField('Name', max_length=60)
	details = models.CharField('Details', max_length=200)
	#due_date = models.DateTimeField('Deadline')
	#date_created = models.DateTimeField(auto_now_add=True)
	is_finished = models.BooleanField(default=False)
	#date_finished = models.DateTimeField('Completion Date')
	#notes = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.name


#TODO: dodać formularze do forms.py
#TODO: dodać daty do modelu i ogarnąć je w formularzach
#TODO: zrobić ładny lay out