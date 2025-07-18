# Generated by Django 5.2.4 on 2025-07-17 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0006_rename_mark_certificatemodel_certificate_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='certificatemodel',
            old_name='date',
            new_name='enddate',
        ),
        migrations.RenameField(
            model_name='educationmodel',
            old_name='date',
            new_name='enddate',
        ),
        migrations.RemoveField(
            model_name='experiencemodel',
            name='date',
        ),
        migrations.AddField(
            model_name='certificatemodel',
            name='startdate',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='educationmodel',
            name='startdate',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='experiencemodel',
            name='enddate',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='experiencemodel',
            name='startdate',
            field=models.DateField(null=True),
        ),
    ]
