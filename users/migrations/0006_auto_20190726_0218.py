# Generated by Django 2.2 on 2019-07-25 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20190725_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='booked',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='airline.Booking'),
        ),
    ]
