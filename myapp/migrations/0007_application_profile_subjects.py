# Generated by Django 5.0.6 on 2024-06-25 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_application_instagram_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='profile_subjects',
            field=models.TextField(blank=True, null=True, verbose_name='Профильные предметы'),
        ),
    ]
