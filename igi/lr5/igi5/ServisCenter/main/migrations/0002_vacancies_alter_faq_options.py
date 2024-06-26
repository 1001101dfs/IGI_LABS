# Generated by Django 5.0.6 on 2024-05-19 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.TextField(verbose_name='ФИО')),
                ('phone', models.TextField(verbose_name='Номер телефона')),
                ('description', models.TextField(verbose_name='Описание выполняемыхх работ')),
            ],
            options={
                'verbose_name': 'Вакансия',
                'verbose_name_plural': 'Вакансии',
            },
        ),
        migrations.AlterModelOptions(
            name='faq',
            options={'verbose_name': 'FAQ', 'verbose_name_plural': 'FAQ'},
        ),
    ]
