# Generated by Django 4.2.7 on 2023-11-26 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_blog', '0003_subscriber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
