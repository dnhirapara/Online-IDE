# Generated by Django 3.0.4 on 2020-08-29 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('IDEApp', '0009_auto_20200830_0011'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TestCases',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('inp', models.TextField()),
                ('out', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20)),
                ('defination', models.TextField()),
                ('submission_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IDEApp.Submission')),
                ('tc_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IDEApp.TestCases')),
            ],
        ),
    ]