# Generated by Django 3.0.4 on 2020-03-28 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corpapp', '0002_auto_20200328_1416'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='state',
            name='bip',
        ),
        migrations.AddField(
            model_name='university',
            name='kind',
            field=models.CharField(default='university', max_length=32),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='state',
            name='abbreviation',
            field=models.CharField(max_length=8),
        ),
    ]