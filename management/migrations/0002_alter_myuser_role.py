# Generated by Django 3.2.4 on 2021-11-06 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='role',
            field=models.SmallIntegerField(choices=[(0, 'Admin'), (1, 'Staff'), (2, 'Normal user')], null=True),
        ),
    ]