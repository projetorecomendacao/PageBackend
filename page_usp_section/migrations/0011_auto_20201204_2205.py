# Generated by Django 2.2.6 on 2020-12-04 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_usp_section', '0010_auto_20201203_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cognitiondeficitusp',
            name='q3_15',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cognitiondeficitusp',
            name='q3_30',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cognitiondeficitusp',
            name='q3_45',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cognitiondeficitusp',
            name='q3_60',
            field=models.TextField(blank=True, null=True),
        ),
    ]