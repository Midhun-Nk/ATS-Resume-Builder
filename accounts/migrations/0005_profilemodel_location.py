# Generated by Django 5.2.4 on 2025-07-19 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_rename_linkedln_profilemodel_linkedin_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilemodel',
            name='location',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
