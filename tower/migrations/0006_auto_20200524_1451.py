# Generated by Django 3.0.5 on 2020-05-24 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tower', '0005_auto_20200524_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='finished',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='operation',
            name='progress',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='operation_type',
            name='allowed',
            field=models.CharField(choices=[('cleaner', 'cleaner'), ('painter', 'painter'), ('plumber', 'plumber')], max_length=30),
        ),
    ]
