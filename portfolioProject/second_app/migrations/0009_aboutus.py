# Generated by Django 3.2.9 on 2022-01-03 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second_app', '0008_teammember'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1', models.CharField(blank=True, max_length=255, null=True)),
                ('field1', models.TextField(blank=True, max_length=999, null=True)),
                ('title2', models.CharField(blank=True, max_length=255, null=True)),
                ('field2', models.TextField(blank=True, max_length=999, null=True)),
                ('title3', models.CharField(blank=True, max_length=255, null=True)),
                ('field3', models.TextField(blank=True, max_length=999, null=True)),
                ('title4', models.CharField(blank=True, max_length=255, null=True)),
                ('field4', models.TextField(blank=True, max_length=999, null=True)),
            ],
        ),
    ]
