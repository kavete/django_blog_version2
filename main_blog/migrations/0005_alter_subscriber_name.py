# Generated by Django 4.2.7 on 2023-11-28 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_blog', '0004_alter_subscriber_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
