# Generated by Django 3.1.6 on 2021-03-19 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esm_program_section', '0002_auto_20210318_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actionsesm',
            name='actionDate',
            field=models.CharField(blank=True, default='1616116047000', max_length=50),
        ),
        migrations.AlterField(
            model_name='editorprogram',
            name='role',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='program',
            name='updateDate',
            field=models.CharField(blank=True, default='1616116047000', max_length=50),
        ),
    ]
