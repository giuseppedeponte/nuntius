# Generated by Django 2.1.7 on 2019-04-23 12:04

from django.db import migrations, models
import nuntius.models


class Migration(migrations.Migration):

    dependencies = [("nuntius", "0011_open_click_counts")]

    operations = [
        migrations.AddField(
            model_name="campaignsentevent",
            name="tracking_id",
            field=models.CharField(
                default=nuntius.models.CampaignSentEvent.generate_tracking_id,
                editable=False,
                max_length=12,
                null=True,
            ),
        )
    ]
