# Generated by Django 4.2.6 on 2023-10-31 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('session_id', models.CharField(blank=True, max_length=255, null=True)),
                ('remote_address', models.CharField(blank=True, max_length=255, null=True)),
                ('remote_host', models.CharField(blank=True, max_length=255, null=True)),
                ('user_agent', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
