# Generated by Django 4.2.1 on 2023-05-14 16:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("app1", "0005_property_email_property_phone_property_user_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="property",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
