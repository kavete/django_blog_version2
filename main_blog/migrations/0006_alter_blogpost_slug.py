# Generated by Django 4.2.7 on 2023-11-28 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_blog', '0005_alter_subscriber_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(blank=True, default='', unique=True),
        ),
    ]
