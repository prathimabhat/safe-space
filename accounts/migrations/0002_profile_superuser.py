# Generated by Django 3.0.7 on 2021-01-03 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='superuser',
            field=models.BooleanField(default=True),
        ),
    ]
