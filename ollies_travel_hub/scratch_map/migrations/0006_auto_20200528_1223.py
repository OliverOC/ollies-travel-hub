# Generated by Django 3.0.6 on 2020-05-28 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scratch_map', '0005_auto_20200528_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='country_code',
            field=models.CharField(max_length=50),
        ),
    ]
