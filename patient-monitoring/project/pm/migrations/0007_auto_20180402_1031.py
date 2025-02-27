# Generated by Django 2.0 on 2018-04-02 10:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.query_utils


class Migration(migrations.Migration):

    dependencies = [
        ('pm', '0006_auto_20180402_1031'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='blood_pressure',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='body_temperature',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='breath_rate',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='date_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='doctor',
            field=models.ForeignKey(limit_choices_to=django.db.models.query_utils.Q(user_type='patient'), null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doctor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='appointment',
            name='prescription',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='prognosis',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='pulse_rate',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='report',
            field=models.TextField(max_length=500, null=True),
        ),
    ]
