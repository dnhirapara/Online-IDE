# Generated by Django 3.0.4 on 2020-08-29 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IDEApp', '0016_remove_submission_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='result',
            field=models.TextField(null=True),
        ),
    ]
