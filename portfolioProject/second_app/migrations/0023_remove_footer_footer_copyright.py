# Generated by Django 3.2.9 on 2022-01-21 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('second_app', '0022_auto_20220106_1845'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='footer',
            name='footer_copyright',
        ),
    ]
