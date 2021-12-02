# Generated by Django 3.2.4 on 2021-11-25 15:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_auto_20211112_1603'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('number', models.SmallIntegerField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='created_at',
            field=models.DateField(default=datetime.date(2021, 11, 25)),
        ),
    ]