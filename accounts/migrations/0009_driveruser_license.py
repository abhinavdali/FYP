# Generated by Django 4.0.3 on 2022-03-07 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_user_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='driveruser',
            name='license',
            field=models.CharField(default=12344, max_length=100),
            preserve_default=False,
        ),
    ]
