# Generated by Django 5.0.6 on 2024-05-23 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_alter_report_options_job_idjob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestid',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]