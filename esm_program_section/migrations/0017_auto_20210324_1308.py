# Generated by Django 3.1.6 on 2021-03-24 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esm_program_section', '0016_auto_20210324_1301'),
    ]

    operations = [
        migrations.AddField(
            model_name='actionsesm',
            name='createDate',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='program',
            name='createDate',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Criado em'),
        ),
        migrations.AddField(
            model_name='program',
            name='updateDateNew',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Criado em'),
        ),
    ]