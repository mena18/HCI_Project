# Generated by Django 3.0.5 on 2020-05-27 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20200526_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('plumber', 'plumber'), ('none', 'none'), ('painter', 'painter'), ('cleaner', 'cleaner')], default='none', max_length=10),
        ),
    ]