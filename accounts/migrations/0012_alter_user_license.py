# Generated by Django 4.0.3 on 2022-03-07 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_alter_driveruser_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='license',
            field=models.CharField(max_length=100, null=True),
        ),
    ]