# Generated by Django 3.1.6 on 2021-03-24 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esm_program_section', '0015_auto_20210324_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actionsesm',
            name='actionDate',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='program',
            name='updateDate',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
