# Generated by Django 3.2.7 on 2021-10-08 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_task_is_finished'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='task_counter',
            field=models.IntegerField(default=0, verbose_name='Counter'),
        ),
    ]
