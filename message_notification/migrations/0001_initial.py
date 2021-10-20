# Generated by Django 3.2.7 on 2021-10-19 20:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isNew', models.BooleanField(choices=[(1, 'True'), (2, 'False')], default=1)),
                ('message', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='message_noti', to='message.message')),
                ('user_notified', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_notified_message', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]