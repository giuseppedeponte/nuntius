# Generated by Django 2.1.5 on 2019-02-05 10:47

import django.db.models.deletion
from django.db import migrations, models

from nuntius import app_settings


class Migration(migrations.Migration):

    dependencies = [("nuntius", "0005_change_status_choices")]

    operations = [
        migrations.AlterField(
            model_name="campaignsentevent",
            name="subscriber",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=app_settings.NUNTIUS_SUBSCRIBER_MODEL,
                verbose_name="Subscriber",
            ),
        )
    ]
