# Generated by Django 2.0.7 on 2020-01-05 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ministering', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='ministerees',
            field=models.ManyToManyField(blank=True, related_name='ministerees', to='directory.Member'),
        ),
    ]