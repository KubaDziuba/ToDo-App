# Generated by Django 3.2.7 on 2021-10-08 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_category_task_counter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='task_counter',
        ),
    ]