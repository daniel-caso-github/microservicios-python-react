# Generated by Django 3.1.3 on 2021-03-27 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='likes',
        ),
        migrations.AddField(
            model_name='products',
            name='links',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
