# Generated by Django 3.0.4 on 2020-03-28 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('corpapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('abbreviation', models.CharField(max_length=3)),
                ('bip', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='university',
            old_name='nstaff',
            new_name='n_staff',
        ),
        migrations.RenameField(
            model_name='university',
            old_name='nstudents',
            new_name='n_students',
        ),
        migrations.AddField(
            model_name='university',
            name='abbreviation',
            field=models.CharField(default='abv', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='university',
            name='budget',
            field=models.IntegerField(default=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='university',
            name='city',
            field=models.CharField(default='city', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='university',
            name='corona_page',
            field=models.CharField(default='coronapage', max_length=600),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='university',
            name='main_page',
            field=models.CharField(default='mainpage', max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='university',
            name='n_profs',
            field=models.IntegerField(default=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='university',
            name='ownership',
            field=models.CharField(default='owner', max_length=10),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('abbreviation', models.CharField(max_length=5)),
                ('bip', models.IntegerField()),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='corpapp.Country')),
            ],
        ),
        migrations.AddField(
            model_name='university',
            name='state',
            field=models.ForeignKey(default='zh', on_delete=django.db.models.deletion.CASCADE, to='corpapp.State'),
            preserve_default=False,
        ),
    ]
