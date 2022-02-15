# Generated by Django 3.2.9 on 2022-01-23 18:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('second_app', '0027_homepageyouget_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False)),
                ('paymentId', models.CharField(blank=True, max_length=264, null=True)),
                ('orderId', models.CharField(blank=True, max_length=200, null=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('order_package', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='second_app.package')),
                ('order_service', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='second_app.services')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
