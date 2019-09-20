# Generated by Django 2.0.7 on 2018-07-20 10:03

from django.db import migrations, models
import django.db.models.deletion
import nuntius.models


class Migration(migrations.Migration):

    dependencies = [("nuntius", "0002_add_mosaico")]

    operations = [
        migrations.AlterField(
            model_name="campaign",
            name="segment_content_type",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="contenttypes.ContentType",
            ),
        ),
        migrations.AlterField(
            model_name="campaign",
            name="segment_id",
            field=models.CharField(max_length=255, null=True),
        ),
    ]
