# Generated by Django 3.0.6 on 2020-06-29 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scratch_map', '0013_auto_20200618_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='trip_img',
            field=models.ImageField(blank=True, default='scratch_map/images/default.jpg', upload_to='scratch_map/images'),
        ),
    ]
