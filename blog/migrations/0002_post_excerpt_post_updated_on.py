# Generated by Django 4.2.17 on 2025-01-06 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='excerpt',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
