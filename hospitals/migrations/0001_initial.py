# Generated by Django 5.1.5 on 2025-02-28 03:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('specialization', models.CharField(max_length=40)),
                ('phone_number', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctors', to='accounts.hospitalprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Scheduled', 'Scheduled'), ('Completed', 'Cancled'), ('Cancled', 'Cancled')], max_length=20)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='accounts.hospitalprofile')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hospital_appointment', to=settings.AUTH_USER_MODEL)),
                ('docotor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='hospitals.doctor')),
            ],
        ),
    ]
