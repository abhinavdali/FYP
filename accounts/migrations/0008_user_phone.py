# Generated by Django 4.0.3 on 2022-03-07 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_customeruser_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(default='1233', max_length=12),
        ),
    ]
