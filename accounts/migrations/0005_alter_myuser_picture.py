# Generated by Django 3.2.7 on 2021-10-07 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_myuser_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='picture',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
