# Generated by Django 4.2.1 on 2023-05-09 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0003_tenant_budget"),
    ]

    operations = [
        migrations.AddField(
            model_name="tenant",
            name="bathrooms",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="tenant",
            name="bedrooms",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]