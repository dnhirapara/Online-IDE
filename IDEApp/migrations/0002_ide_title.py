# Generated by Django 3.0.4 on 2020-08-19 17:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('IDEApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ide',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]