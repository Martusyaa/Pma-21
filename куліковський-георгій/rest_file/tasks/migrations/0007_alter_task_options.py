# Generated by Django 4.2.4 on 2023-08-20 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_alter_task_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ('is_completed', 'title'), 'verbose_name': 'task', 'verbose_name_plural': 'tasks'},
        ),
    ]
