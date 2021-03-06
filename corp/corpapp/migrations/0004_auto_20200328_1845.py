# Generated by Django 3.0.4 on 2020-03-28 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('corpapp', '0003_auto_20200328_1512'),
    ]

    operations = [
        migrations.RenameField(
            model_name='university',
            old_name='quality',
            new_name='page_quality',
        ),
        migrations.AddField(
            model_name='country',
            name='people',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='state',
            name='people',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Corporation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('kind', models.CharField(max_length=32)),
                ('n_employees', models.IntegerField()),
                ('city', models.CharField(max_length=64)),
                ('stock_price', models.IntegerField()),
                ('corona_page', models.CharField(max_length=600)),
                ('main_page', models.CharField(max_length=128)),
                ('page_quality', models.CharField(max_length=12)),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='corpapp.State')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('people', models.IntegerField()),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='corpapp.State')),
            ],
        ),
    ]
