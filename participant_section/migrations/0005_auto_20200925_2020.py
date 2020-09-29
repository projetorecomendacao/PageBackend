# Generated by Django 2.2.6 on 2020-09-25 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participant_section', '0004_auto_20200911_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participantsituation',
            name='p11_retire_more_time_activity',
            field=models.CharField(blank='True', max_length=100, null=True, verbose_name='Se aposentado, qual profissão exerceu por mais tempo'),
        ),
        migrations.AlterField(
            model_name='participantsituation',
            name='p13_income_F',
            field=models.CharField(choices=[['BPC', 'BPC'], ['Até um salário mínimo', 'Até um salário mínimo'], ['Entre 1 e 2 salários mínimos', 'Entre 1 e 2 salários mínimos'], ['Entre 2 e 3 salários mínimos', 'Entre 2 e 3 salários mínimos'], ['Entre 3 e 4 salários mínimos', 'Entre 3 e 4 salários mínimos'], ['Entre 4 e 5 salários mínimos', 'Entre 4 e 5 salários mínimos'], ['Entre 5 e 10 salários mínimos', 'Entre 5 e 10 salários mínimos'], ['mais de 10 salários mínimos', 'mais de 10 salários mínimos'], ['prefere não informar', 'prefere não informar']], max_length=70, verbose_name='Rendimento Mensal Familiar:'),
        ),
        migrations.AlterField(
            model_name='participantsituation',
            name='p13_income_I',
            field=models.CharField(choices=[['BPC', 'BPC'], ['Até um salário mínimo', 'Até um salário mínimo'], ['Entre 1 e 2 salários mínimos', 'Entre 1 e 2 salários mínimos'], ['Entre 2 e 3 salários mínimos', 'Entre 2 e 3 salários mínimos'], ['Entre 3 e 4 salários mínimos', 'Entre 3 e 4 salários mínimos'], ['Entre 4 e 5 salários mínimos', 'Entre 4 e 5 salários mínimos'], ['Entre 5 e 10 salários mínimos', 'Entre 5 e 10 salários mínimos'], ['mais de 10 salários mínimos', 'mais de 10 salários mínimos'], ['prefere não informar', 'prefere não informar']], max_length=70, verbose_name='Rendimento Mensal Individual:'),
        ),
        migrations.AlterField(
            model_name='participantsituation',
            name='p15_religion',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Religião'),
        ),
    ]
