# Generated by Django 3.2.4 on 2021-09-09 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0004_absensi_kontrolabsensi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='absensi',
            name='kontrolabsensi',
        ),
        migrations.AddField(
            model_name='absensi',
            name='kontrolabsensi',
            field=models.ManyToManyField(to='myapi.Kontrolabsensi'),
        ),
    ]
