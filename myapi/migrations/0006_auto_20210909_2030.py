# Generated by Django 3.2.4 on 2021-09-09 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0005_auto_20210909_2024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='absensi',
            name='kontrolabsensi',
        ),
        migrations.AddField(
            model_name='absensi',
            name='kontrolabsensi',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapi.kontrolabsensi'),
        ),
    ]
