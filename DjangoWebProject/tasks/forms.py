from django import forms
from .models import *


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['cat_name']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['category', 'name', 'details', 'is_finished']
