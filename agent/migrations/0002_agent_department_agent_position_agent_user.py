# Generated by Django 4.2.1 on 2023-05-24 04:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("agent", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="agent",
            name="department",
            field=models.CharField(default="Agent", max_length=100),
        ),
        migrations.AddField(
            model_name="agent",
            name="position",
            field=models.CharField(default="Agent", max_length=100),
        ),
        migrations.AddField(
            model_name="agent",
            name="user",
            field=models.OneToOneField(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
