# Generated by Django 3.2.7 on 2021-10-17 21:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('review_comment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviewcomment',
            name='user',
        ),
        migrations.AddField(
            model_name='reviewcomment',
            name='user_created',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_created', to=settings.AUTH_USER_MODEL),
        ),
    ]
