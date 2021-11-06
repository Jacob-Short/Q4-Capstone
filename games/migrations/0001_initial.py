# Generated by Django 3.2.7 on 2021-11-06 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('slug', models.CharField(max_length=150)),
                ('rating', models.CharField(choices=[('poor', 'poor'), ('good', 'good'), ('great', 'great'), ('exceptional', 'exceptional')], max_length=150)),
                ('platform', models.CharField(choices=[('xbox', 'xbox'), ('playstation', 'playstation'), ('pc', 'pc'), ('switch', 'switch')], max_length=150)),
                ('released_at', models.DateField(blank=True, null=True)),
                ('image_background', models.ImageField(upload_to='images/')),
                ('isNew', models.BooleanField(default=True)),
            ],
        ),
    ]
