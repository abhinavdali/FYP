# Generated by Django 4.0.3 on 2022-03-08 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_remove_customeruser_username_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customeruser',
            name='password',
        ),
        migrations.RemoveField(
            model_name='driveruser',
            name='password',
        ),
    ]
