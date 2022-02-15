# Generated by Django 3.2.9 on 2022-01-02 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('second_app', '0003_ecommerceservie'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasicProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_doller', models.CharField(blank=True, max_length=100, null=True)),
                ('amonut_tk', models.CharField(blank=True, max_length=100, null=True)),
                ('disk_space', models.BooleanField(blank=True, default=True, help_text='50GB disk space', null=True)),
                ('email_account', models.BooleanField(blank=True, default=True, help_text='50 Email Account', null=True)),
                ('bandwith', models.BooleanField(blank=True, default=True, help_text='50GB disk spacet', null=True)),
                ('maintenance', models.BooleanField(blank=True, default=True, null=True)),
                ('subdomain', models.BooleanField(blank=True, default=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=222)),
                ('basic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='second_app.basicproduct')),
            ],
        ),
        migrations.CreateModel(
            name='ProProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_doller', models.CharField(blank=True, max_length=100, null=True)),
                ('amonut_tk', models.CharField(blank=True, max_length=100, null=True)),
                ('disk_space', models.BooleanField(blank=True, default=True, help_text='50GB disk space', null=True)),
                ('email_account', models.BooleanField(blank=True, default=True, help_text='50 Email Account', null=True)),
                ('bandwith', models.BooleanField(blank=True, default=True, help_text='50GB disk spacet', null=True)),
                ('maintenance', models.BooleanField(blank=True, default=True, null=True)),
                ('subdomain', models.BooleanField(blank=True, default=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StanderdProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_doller', models.CharField(blank=True, max_length=100, null=True)),
                ('amonut_tk', models.CharField(blank=True, max_length=100, null=True)),
                ('disk_space', models.BooleanField(blank=True, default=True, help_text='50GB disk space', null=True)),
                ('email_account', models.BooleanField(blank=True, default=True, help_text='50 Email Account', null=True)),
                ('bandwith', models.BooleanField(blank=True, default=True, help_text='50GB disk spacet', null=True)),
                ('maintenance', models.BooleanField(blank=True, default=True, null=True)),
                ('subdomain', models.BooleanField(blank=True, default=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='service',
            name='user',
        ),
        migrations.DeleteModel(
            name='EcommerceServie',
        ),
        migrations.DeleteModel(
            name='Service',
        ),
        migrations.AddField(
            model_name='product',
            name='pro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='second_app.proproduct'),
        ),
        migrations.AddField(
            model_name='product',
            name='standerd',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='second_app.standerdproduct'),
        ),
    ]