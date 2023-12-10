# Generated by Django 4.2.7 on 2023-12-09 22:35

from django.db import migrations, models
import django_ckeditor_5.fields


class Migration(migrations.Migration):
    dependencies = [
        ("dashboard", "0003_emailcampaign"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="emailcampaign",
            name="recipients",
        ),
        migrations.AddField(
            model_name="emailcampaign",
            name="subscrioption_type",
            field=models.CharField(
                blank=True,
                choices=[
                    ("monthly", "Monthly"),
                    ("yearly", "Yearly"),
                    ("enterprise", "Enterprise"),
                    ("free", "Free"),
                    ("all", "all"),
                ],
                max_length=10,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="emailcampaign",
            name="message",
            field=django_ckeditor_5.fields.CKEditor5Field(),
        ),
    ]
