# Generated by Django 2.2.6 on 2020-05-28 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_usp_section', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AgingAspectsUsp',
        ),
        migrations.RenameField(
            model_name='lowsocialsupportusp',
            old_name='low_social_support',
            new_name='low_social_support_obs',
        ),
        migrations.RemoveField(
            model_name='cognitiondeficitusp',
            name='q3_language_function_attention',
        ),
        migrations.RemoveField(
            model_name='cognitiondeficitusp',
            name='q3_language_function_attention_score',
        ),
        migrations.RemoveField(
            model_name='cognitiondeficitusp',
            name='q4_visospatial_ability_score',
        ),
        migrations.RemoveField(
            model_name='pageusp',
            name='health_monitoring',
        ),
        migrations.AddField(
            model_name='biologicalaspectsusp',
            name='score',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='cardiovascularfactorsusp',
            name='score',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='cognitiondeficitusp',
            name='score',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='depressionusp',
            name='score',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='functionaldisabilityusp',
            name='score',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='malnutritionusp',
            name='score',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='misusemedicationsusp',
            name='q44_diseases_last_5_years_l_other',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='l)Outra?'),
        ),
        migrations.AddField(
            model_name='misusemedicationsusp',
            name='q45_health_problems_h_other',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='h)Outro?'),
        ),
        migrations.AddField(
            model_name='misusemedicationsusp',
            name='score',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='negativeattitudesagingusp',
            name='score',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='sensorydeficitusp',
            name='score',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='misusemedicationsusp',
            name='q44_diseases_last_5_years_l',
            field=models.CharField(choices=[['S', 'Sim'], ['N', 'Não']], default='N', max_length=1, verbose_name='l)Outra?'),
        ),
        migrations.AlterField(
            model_name='misusemedicationsusp',
            name='q45_health_problems_h',
            field=models.CharField(choices=[['S', 'Sim'], ['N', 'Não']], default='N', max_length=1, verbose_name='h)Outro?'),
        ),
        migrations.RemoveField(
            model_name='misusemedicationsusp',
            name='q46_medicines',
        ),
        migrations.AddField(
            model_name='misusemedicationsusp',
            name='q46_medicines',
            field=models.TextField(null=True, verbose_name='Medicamentos'),
        ),
    ]