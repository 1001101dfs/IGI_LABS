# Generated by Django 5.0.6 on 2024-05-21 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_request_requestid_remove_job_make'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestid',
            name='cost',
            field=models.IntegerField(null=True, verbose_name='Стоимость'),
        ),
    ]