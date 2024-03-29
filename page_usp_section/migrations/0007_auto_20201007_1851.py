# Generated by Django 2.2.6 on 2020-10-07 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_usp_section', '0006_auto_20201007_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='malnutritionusp',
            name='d33_lost_weight_no_reason_amount',
            field=models.CharField(choices=[['Não', 'Não'], ['Não sabe', 'Não sabe'], ['Mais de 3 KG', 'Mais de 3 Kg'], ['Entre 1 e 3 KG', 'Entre 1 e 3 KG']], default='N', max_length=15, verbose_name='33. O(A) senhor(a) tem histórico familiar (1º grau) de DCV (infarto, derrama e/ou angina) ?'),
        ),
        migrations.AlterField(
            model_name='malnutritionusp',
            name='d33_lost_weight_no_reason',
            field=models.CharField(choices=[['S', 'Sim'], ['N', 'Não']], default='N', max_length=1, verbose_name='33. O(A) senhor(a) tem histórico familiar (1º grau) de DCV (infarto, derrama e/ou angina) ?'),
        ),
    ]
