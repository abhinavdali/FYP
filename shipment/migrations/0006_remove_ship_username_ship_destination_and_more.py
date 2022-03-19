# Generated by Django 4.0.3 on 2022-03-19 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipment', '0005_alter_ship_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ship',
            name='username',
        ),
        migrations.AddField(
            model_name='ship',
            name='destination',
            field=models.CharField(default='lol', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ship',
            name='phone_number',
            field=models.CharField(default='123123', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ship',
            name='receiver',
            field=models.CharField(default='lol', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ship',
            name='start',
            field=models.CharField(default='lol', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ship',
            name='status',
            field=models.CharField(default='lol', max_length=100),
            preserve_default=False,
        ),
    ]