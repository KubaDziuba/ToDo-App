from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from tasks.models import Task, Category
from django.views import View
from tasks.forms import TaskForm
from django.views.generic import UpdateView, DetailView


class NewTask(View):
	def get(self, request):
		form = TaskForm()
		categories = Category.objects.all()
		context = {'categories': categories, 'form': form}
		return render(request, 'tasks/newtask.html', context)

	def post(self, request):
		form = TaskForm(request.POST)
		if form.is_valid():
			task = Task.objects.create(
				category=form.cleaned_data.get('category'),
				name=form.cleaned_data.get('name'),
				details=form.cleaned_data.get('details'),
				is_finished=form.cleaned_data.get('is_finished')
			)
			chosen_category = Category.objects.get(cat_name=form.cleaned_data.get('category'))
			#current_cat_counter = chosen_category.task_counter
			#current_cat_counter += 1
			#chosen_category.task_counter = current_cat_counter
			chosen_category.save()
			return HttpResponseRedirect(reverse('tasks:index'))


class UpdateTask(UpdateView):
	def get(self, request, task_id):
		form = TaskForm()
		current_task = Task.objects.get(pk=task_id)
		categories = Category.objects.all()
		context = {'current_task': current_task, 'categories': categories, 'form': form}
		return render(request, 'tasks/update_task.html', context)

	def post(self, request, task_id):
		categories = Category.objects.all()
		current_task = Task.objects.get(pk=task_id)
		assigned_cat = request.POST['category_list']
		category = Category.objects.get(cat_name=assigned_cat)
		taskname = request.POST['new_task']
		taskdesc = request.POST['new_task_desc']
		current_task.category = category
		current_task.name = taskname
		current_task.details = taskdesc
		current_task.save()
		context = {'current_task': current_task, 'categories': categories}
		return HttpResponseRedirect(reverse('tasks:task_details', args=(current_task.id,)))


def task_details(request, task_id):
	selected_task = Task.objects.get(pk=task_id)
	categories = Category.objects.all()
	context = {'selected_task': selected_task, 'categories': categories}
	return render(request, 'tasks/task_detail.html', context)


def close_task(request, task_id):
	current_task = Task.objects.get(pk=task_id)
	current_task.is_finished = True
	current_task.save()
	return HttpResponseRedirect(reverse('tasks:index'))


def delete_task(request, task_id):
	current_task = Task.objects.get(pk=task_id)
	current_task.delete()
	return HttpResponseRedirect(reverse('tasks:index'))
