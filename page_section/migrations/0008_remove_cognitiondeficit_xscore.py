# Generated by Django 2.2.6 on 2020-09-14 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page_section', '0007_cognitiondeficit_xscore'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cognitiondeficit',
            name='xscore',
        ),
    ]
