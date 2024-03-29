# Generated by Django 2.2.6 on 2020-12-03 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_usp_section', '0009_auto_20201203_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardiovascularfactorsusp',
            name='q37_hypertension_unknow',
            field=models.CharField(blank=True, choices=[['S', 'Sim'], ['N', 'Não']], default='N', max_length=1, null=True, verbose_name='34. O(a) senhor(a) tem hipertensão arterial descontrolada? [Pontuar como sim quando PA auto referida for                    superior a 140/90 mmHg ou caso o(a) idoso(a) não saiba informar.]'),
        ),
        migrations.AlterField(
            model_name='cardiovascularfactorsusp',
            name='q38_uncontrolled_diabetes_unknow',
            field=models.CharField(blank=True, choices=[['S', 'Sim'], ['N', 'Não']], default='N', max_length=1, null=True, verbose_name='34. O(a) senhor(a) tem hipertensão arterial descontrolada? [Pontuar como sim quando PA auto referida for                    superior a 140/90 mmHg ou caso o(a) idoso(a) não saiba informar.]'),
        ),
        migrations.AlterField(
            model_name='cardiovascularfactorsusp',
            name='q39_cholesterol_unknow',
            field=models.CharField(blank=True, choices=[['S', 'Sim'], ['N', 'Não']], default='N', max_length=1, null=True, verbose_name='34. O(a) senhor(a) tem hipertensão arterial descontrolada? [Pontuar como sim quando PA auto referida for                    superior a 140/90 mmHg ou caso o(a) idoso(a) não saiba informar.]'),
        ),
    ]
