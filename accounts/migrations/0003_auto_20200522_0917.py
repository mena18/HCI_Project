# Generated by Django 3.0.5 on 2020-05-22 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('plumber', 'plumber'), ('painter', 'painter'), ('none', 'none'), ('cleaner', 'cleaner')], default='none', max_length=10),
        ),
    ]
