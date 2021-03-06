# Generated by Django 3.2.6 on 2021-08-14 06:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ajaxapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='library',
            name='publish',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='library',
            name='timeStamp',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
