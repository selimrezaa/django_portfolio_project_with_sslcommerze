# Generated by Django 3.2 on 2021-06-25 14:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0010_remove_teammember_short_info'),
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
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Delivered', 'Delivered')], default='Pending', max_length=255)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.client')),
            ],
        ),
    ]