# Generated by Django 3.2.9 on 2022-01-23 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second_app', '0025_package_demo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='demo',
            field=models.URLField(blank=True),
        ),
    ]