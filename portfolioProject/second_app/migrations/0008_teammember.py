# Generated by Django 3.2.9 on 2022-01-03 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second_app', '0007_alter_worklist_work'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.FileField(blank=True, null=True, upload_to='teammember')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('subtitle', models.CharField(blank=True, max_length=255, null=True)),
                ('describe', models.TextField(blank=True, max_length=999, null=True)),
                ('facebook_link', models.URLField(blank=True, max_length=999, null=True)),
                ('instagram_link', models.URLField(blank=True, max_length=999, null=True)),
                ('whatsapp_link', models.URLField(blank=True, max_length=999, null=True)),
            ],
        ),
    ]