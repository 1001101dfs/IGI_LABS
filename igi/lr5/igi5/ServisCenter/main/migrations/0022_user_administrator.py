# Generated by Django 5.0.6 on 2024-05-22 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_alter_contacts_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='administrator',
            field=models.BooleanField(default=False, verbose_name='Работник'),
        ),
    ]
