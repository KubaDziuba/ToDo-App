from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from tasks.models import Category, Task
from django.views import View
from tasks.forms import CategoryForm
from django.db.models import Count
from django.views.generic import UpdateView


class NewCategory(View):
	def get(self, request):
		form = CategoryForm()
		categories = Category.objects.all()
		context = {'categories': categories, 'form': form}
		return render(request, 'tasks/newcategory.html', context)

	def post(self, request):
		form = CategoryForm(request.POST)
		if form.is_valid():
			category = Category.objects.create(
				cat_name=form.cleaned_data.get('cat_name')
			)
			return HttpResponseRedirect(reverse('tasks:index'))


def category_list(request):
	categories = Category.objects.annotate(num_tasks=Count('task'))
	context = {'categories': categories}
	return render(request, 'tasks/categories.html', context)


#def category_detail(request, category_id):
#	categories = Category.objects.all()
#	selected_category = Category.objects.get(pk=category_id)
#	context = {'selected_category': selected_category, 'categories': categories}
#	return render(request, 'tasks/category_detail.html', context)


def delete_category(request, category_id):
	current_category = Category.objects.get(pk=category_id)
	current_category.delete()
	return HttpResponseRedirect(reverse('tasks:category_list'))


class UpdateCategory(UpdateView):
	def get(self, request, category_id):
		categories = Category.objects.all()
		form = CategoryForm
		current_category = Category.objects.get(pk=category_id)
		context = {'categories': categories, 'current_category': current_category, 'form': form}
		return render(request, 'tasks/updatecategory.html', context)

	def post(self, request, category_id):
		categories = Category.objects.all()
		current_category = Category.objects.get(pk=category_id)
		category_name =  request.POST['new_category']
		current_category.cat_name = category_name
		current_category.save()
		context = {'categories': categories}
		return HttpResponseRedirect(reverse('tasks:category_list'))