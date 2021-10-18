# Generated by Django 3.2.7 on 2021-10-18 22:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('faq', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isNew', models.BooleanField(choices=[(1, 'True'), (2, 'False')], default=1)),
                ('faq', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='faq_noti', to='faq.userfaq')),
                ('user_notified', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_notified_faq', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
