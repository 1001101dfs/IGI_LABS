# Generated by Django 5.0.6 on 2024-05-23 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_user_administrator'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Отчёт')),
                ('userId', models.IntegerField(verbose_name='Id работника')),
            ],
        ),
    ]
