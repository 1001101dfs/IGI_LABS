# Generated by Django 5.0.6 on 2024-05-23 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_alter_requestid_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestid',
            name='idReq',
            field=models.IntegerField(null=True, verbose_name='Id заказа'),
        ),
        migrations.AlterField(
            model_name='requestid',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]