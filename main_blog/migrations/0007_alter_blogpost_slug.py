# Generated by Django 4.2.7 on 2023-11-28 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_blog', '0006_alter_blogpost_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(default='', unique=True),
        ),
    ]