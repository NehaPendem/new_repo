# Generated by Django 2.2.2 on 2020-06-22 16:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20200622_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='hr_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
