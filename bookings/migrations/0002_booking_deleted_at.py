# Generated by Django 3.2.9 on 2021-11-24 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='deleted_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
