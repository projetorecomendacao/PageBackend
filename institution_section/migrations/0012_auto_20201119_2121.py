# Generated by Django 2.2.6 on 2020-11-19 21:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('institution_section', '0011_auto_20201119_1113'),
    ]

    operations = [
        migrations.RenameField(
            model_name='webaddress',
            old_name='digitalAddress',
            new_name='digital_address',
        ),
    ]
