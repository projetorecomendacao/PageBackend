# Generated by Django 2.2.6 on 2020-09-14 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_section', '0008_remove_cognitiondeficit_xscore'),
    ]

    operations = [
        migrations.AddField(
            model_name='cognitiondeficit',
            name='score',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
