# Generated by Django 2.2.6 on 2020-09-11 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment_section', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demandmap',
            name='created_at',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='demandmap',
            name='updated_at',
            field=models.DateField(null=True),
        ),
    ]
