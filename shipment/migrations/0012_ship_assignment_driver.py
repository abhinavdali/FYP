# Generated by Django 4.0.3 on 2022-04-13 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_driveruser_vehicle_number_user_vehicle_number'),
        ('shipment', '0011_ship_delivery_date_alter_ship_email_alter_ship_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ship',
            name='assignment_driver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.driveruser'),
        ),
    ]
