# Generated by Django 4.2.7 on 2023-12-15 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_alter_emailcampaign_recipients_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='documents',
            name='model',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]