# Generated by Django 5.0.6 on 2024-05-23 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_report'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='report',
            options={'verbose_name': 'Отчёт', 'verbose_name_plural': 'Отчёты'},
        ),
        migrations.AddField(
            model_name='job',
            name='idJob',
            field=models.IntegerField(null=True, verbose_name='id улсги'),
        ),
    ]
