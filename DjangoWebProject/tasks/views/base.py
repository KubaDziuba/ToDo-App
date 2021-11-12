from django.shortcuts import render, get_object_or_404
from tasks.models import Task, Category


def index(request):
	all_tasks = Task.objects.all()
	categories = Category.objects.all()
	context = {'all_tasks': all_tasks, 'categories': categories}
	return render(request, 'tasks/index.html', context)


def categorized(request, category_id):
	categorized_tasks = Task.objects.filter(category=category_id)
	categories = Category.objects.all()
	selected_category = Category.objects.get(pk=category_id)
	context = {'categorized_tasks': categorized_tasks, 'categories': categories, 'selected_category': selected_category}
	return render(request, 'tasks/categorized.html', context)
