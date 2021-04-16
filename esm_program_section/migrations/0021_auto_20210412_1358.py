# Generated by Django 3.1.6 on 2021-04-12 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esm_program_section', '0020_auto_20210324_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='intervention',
            name='complexConditions',
            field=models.ManyToManyField(blank=True, null=True, to='esm_program_section.ComplexCondition'),
        ),
        migrations.AlterField(
            model_name='intervention',
            name='next',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='intervention',
            name='orderPosition',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='intervention',
            name='statement',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
