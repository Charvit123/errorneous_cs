# Generated by Django 3.1.7 on 2021-03-08 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0003_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='views',
        ),
    ]
