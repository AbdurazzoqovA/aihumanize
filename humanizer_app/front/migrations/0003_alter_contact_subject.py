# Generated by Django 4.2.7 on 2023-12-01 13:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("front", "0002_contact"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="subject",
            field=models.CharField(max_length=150, null=True),
        ),
    ]
