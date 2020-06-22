# Generated by Django 3.0.6 on 2020-05-20 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scratch_map', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='id',
        ),
        migrations.AlterField(
            model_name='country',
            name='country_name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='trip',
            name='country_visited',
            field=models.ForeignKey(default='Germany', on_delete=django.db.models.deletion.CASCADE, related_name='trip', to='scratch_map.Country'),
        ),
    ]