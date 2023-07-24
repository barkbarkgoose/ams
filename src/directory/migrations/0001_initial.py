# Generated by Django 2.0.7 on 2020-01-03 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Household',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('number', models.TextField()),
                ('email', models.TextField()),
                ('priority', models.BooleanField()),
                ('household', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='directory.Household')),
            ],
        ),
    ]
