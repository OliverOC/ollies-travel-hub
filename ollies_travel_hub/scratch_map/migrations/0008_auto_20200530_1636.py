# Generated by Django 3.0.6 on 2020-05-30 16:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('scratch_map', '0007_auto_20200530_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='trip',
            name='country_visited',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='trip', to='scratch_map.Country'),
        ),
    ]