# Generated by Django 5.0.6 on 2024-06-22 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_interviewschedule_access_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speciality',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='speciality',
            name='school',
            field=models.CharField(max_length=100),
        ),
    ]
