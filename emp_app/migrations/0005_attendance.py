# Generated by Django 4.2.7 on 2024-01-21 16:28

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0004_alter_employee_date_of_joining'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('in_time', models.CharField(blank=True, max_length=5, null=True)),
                ('out_time', models.CharField(blank=True, max_length=5, null=True)),
                ('emp_date', models.DateField(default=datetime.date(2024, 1, 21))),
                ('status', models.CharField(default='P', max_length=1)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emp_app.employee')),
            ],
        ),
    ]
