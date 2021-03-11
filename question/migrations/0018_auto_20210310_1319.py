# Generated by Django 3.1.7 on 2021-03-10 07:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('question', '0017_likequestion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='like',
        ),
        migrations.AddField(
            model_name='question',
            name='like',
            field=models.ManyToManyField(blank=True, default=None, related_name='question_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
