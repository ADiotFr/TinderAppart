# Generated by Django 4.2.1 on 2023-05-14 16:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("app1", "0004_tenant_bathrooms_tenant_bedrooms"),
    ]

    operations = [
        migrations.AddField(
            model_name="property",
            name="email",
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name="property",
            name="phone",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name="property",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="tenant",
            name="photo",
            field=models.ImageField(blank=True, null=True, upload_to="tenants_photos"),
        ),
    ]
