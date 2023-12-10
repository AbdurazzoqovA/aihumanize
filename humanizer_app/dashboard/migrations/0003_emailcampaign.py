# Generated by Django 4.2.7 on 2023-12-09 22:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dashboard", "0002_documents_document_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="EmailCampaign",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("subject", models.CharField(max_length=255)),
                ("message", models.TextField()),
                ("sent_at", models.DateTimeField(auto_now_add=True)),
                ("recipients", models.JSONField()),
                ("completed", models.BooleanField(default=False)),
            ],
        ),
    ]
