# Generated by Django 4.2.6 on 2023-10-31 21:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('question', models.CharField(max_length=255)),
                ('response', models.CharField(max_length=255)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.clientmodel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Chat',
        ),
    ]
