# Generated by Django 2.2.4 on 2019-10-19 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('participant_section', '0002_auto_20191001_2252'),
    ]

    operations = [
        migrations.RenameField(
            model_name='participant',
            old_name='p02_adress',
            new_name='p02_address',
        ),
    ]
