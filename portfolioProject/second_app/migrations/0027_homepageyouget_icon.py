# Generated by Django 3.2.9 on 2022-01-23 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second_app', '0026_alter_package_demo'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepageyouget',
            name='icon',
            field=models.CharField(default='fa fa-envelope-open', max_length=100),
        ),
    ]
