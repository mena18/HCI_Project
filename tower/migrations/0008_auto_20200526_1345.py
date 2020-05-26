# Generated by Django 3.0.5 on 2020-05-26 13:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tower', '0007_auto_20200524_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='operation_type',
            name='level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tower.Level'),
        ),
        migrations.AlterField(
            model_name='operation',
            name='worker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='operation_type',
            name='allowed',
            field=models.CharField(choices=[('plumber', 'plumber'), ('painter', 'painter'), ('cleaner', 'cleaner')], max_length=30),
        ),
    ]
