# Generated by Django 4.2.6 on 2023-11-05 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_alter_chatmodel_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmodel',
            name='question',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='chatmodel',
            name='response',
            field=models.CharField(max_length=500),
        ),
    ]
