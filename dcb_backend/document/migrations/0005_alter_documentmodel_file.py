# Generated by Django 4.2.6 on 2023-11-10 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0004_alter_documentmodel_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentmodel',
            name='file',
            field=models.FileField(upload_to='uploads'),
        ),
    ]
