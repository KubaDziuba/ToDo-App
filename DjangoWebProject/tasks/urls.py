from django.urls import path
from . import views


app_name = 'tasks'
urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:category_id>/', views.categorized, name='categorized'),
    path('newcategory/', views.NewCategory.as_view(), name='newcategory'),
    path('newtask/', views.NewTask.as_view(), name='newtask'),
    path('<int:task_id>/details/', views.task_details, name='task_details'),
    path('<int:task_id>/close/', views.close_task, name='close_task'),
    path('<int:task_id>/delete/', views.delete_task, name='delete_task'),
    path('<int:task_id>/update/', views.UpdateTask.as_view(), name='update_task'),
    path('categories/', views.category_list, name='category_list'),
    path('categories/<int:category_id>/delete/', views.delete_category, name='delete_category'),
    path('categories/<int:category_id>/update/', views.UpdateCategory.as_view(), name='updatecategory'),
    ]
