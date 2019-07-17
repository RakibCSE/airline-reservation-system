# Generated by Django 2.2 on 2019-07-17 19:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Travelling',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight', models.CharField(max_length=60)),
                ('from_place', models.CharField(max_length=20)),
                ('to_place', models.CharField(max_length=20)),
                ('departure_time', models.TimeField()),
                ('arrival_time', models.TimeField()),
                ('total_seat', models.IntegerField()),
                ('available_seat', models.IntegerField()),
                ('ticket_rate', models.IntegerField()),
                ('total_collected', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_seats', models.IntegerField()),
                ('cost', models.IntegerField(default=0)),
                ('Travelling', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='airline.Travelling')),
                ('booked', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
