# Generated by Django 3.0.4 on 2020-03-28 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corpapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='university',
            name='main_page',
            field=models.CharField(max_length=128),
        ),
    ]
