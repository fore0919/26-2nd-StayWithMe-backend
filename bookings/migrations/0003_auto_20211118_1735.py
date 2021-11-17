# Generated by Django 3.2.9 on 2021-11-18 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_auto_20211117_1822'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'booking_statuses',
            },
        ),
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bookings.bookingstatus'),
        ),
    ]