# Generated by Django 4.0.3 on 2022-03-07 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_customeruser_password_customeruser_username_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customeruser',
            name='username',
        ),
        migrations.RemoveField(
            model_name='driveruser',
            name='username',
        ),
    ]