# Generated by Django 2.2.4 on 2019-09-20 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_section', '0004_depression_need_investigation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cognitiondeficit',
            old_name='maxScore',
            new_name='max_score',
        ),
        migrations.RenameField(
            model_name='negativeattitudesaging',
            old_name='maxScore',
            new_name='max_score',
        ),
        migrations.RenameField(
            model_name='psychologicalaspects',
            old_name='cognitionDeficit',
            new_name='cognition_deficit',
        ),
        migrations.RenameField(
            model_name='psychologicalaspects',
            old_name='maxScore',
            new_name='max_score',
        ),
        migrations.RenameField(
            model_name='psychologicalaspects',
            old_name='negativeAttitudesAging',
            new_name='negative_attitudes_aging',
        ),
        migrations.RemoveField(
            model_name='cognitiondeficit',
            name='q3LanguageFunctionAttention',
        ),
        migrations.RemoveField(
            model_name='cognitiondeficit',
            name='q4VisospatialAbility',
        ),
        migrations.RemoveField(
            model_name='cognitiondeficit',
            name='q4VisospatialAbilityScore',
        ),
        migrations.RemoveField(
            model_name='cognitiondeficit',
            name='q5Praxia',
        ),
        migrations.RemoveField(
            model_name='cognitiondeficit',
            name='q6MemoryTest',
        ),
        migrations.RemoveField(
            model_name='negativeattitudesaging',
            name='q7AgeSelfPerception',
        ),
        migrations.RemoveField(
            model_name='negativeattitudesaging',
            name='q7AgeSelfPerceptionAnalyze',
        ),
        migrations.RemoveField(
            model_name='negativeattitudesaging',
            name='q7AgeSelfPerceptionWhy',
        ),
        migrations.RemoveField(
            model_name='negativeattitudesaging',
            name='q8AgingAnalyse',
        ),
        migrations.RemoveField(
            model_name='negativeattitudesaging',
            name='q8AgingNegativePoints',
        ),
        migrations.RemoveField(
            model_name='negativeattitudesaging',
            name='q8AgingPositivePoints',
        ),
        migrations.AddField(
            model_name='cognitiondeficit',
            name='need_investigation',
            field=models.CharField(choices=[['S', 'Sim'], ['N', 'Não']], default='N', max_length=1, verbose_name='Necessita Investigação?'),
        ),
        migrations.AddField(
            model_name='cognitiondeficit',
            name='q3_language_function_attention',
            field=models.CharField(choices=[['S', 'Sim'], ['N', 'Não']], default='N', max_length=1, verbose_name='3.Linguagem, função executiva e atenção'),
        ),
        migrations.AddField(
            model_name='cognitiondeficit',
            name='q4_visospatial_ability',
            field=models.CharField(choices=[['S', 'Sim'], ['N', 'Não']], default='N', max_length=1, verbose_name='4. Habilidade visuoespacial'),
        ),
        migrations.AddField(
            model_name='cognitiondeficit',
            name='q4_visospatial_ability_score',
            field=models.IntegerField(default=0, verbose_name='4. Habilidade visuoespacial - Pontuação'),
        ),
        migrations.AddField(
            model_name='cognitiondeficit',
            name='q5_praxia',
            field=models.CharField(choices=[['S', 'Sim'], ['N', 'Não']], default='N', max_length=1, verbose_name='5.Praxia'),
        ),
        migrations.AddField(
            model_name='cognitiondeficit',
            name='q6_memory_test',
            field=models.CharField(choices=[['S', 'Sim'], ['N', 'Não']], default='N', max_length=1, verbose_name='6.Memória'),
        ),
        migrations.AddField(
            model_name='negativeattitudesaging',
            name='need_investigation',
            field=models.CharField(choices=[['S', 'Sim'], ['N', 'Não']], default='N', max_length=1, verbose_name='Necessita Investigação?'),
        ),
        migrations.AddField(
            model_name='negativeattitudesaging',
            name='q7_age_self_perception',
            field=models.IntegerField(blank=True, null=True, verbose_name='7.Que idade o(a) senhor(a) sente ter? '),
        ),
        migrations.AddField(
            model_name='negativeattitudesaging',
            name='q7_age_self_perception_analyze',
            field=models.CharField(choices=[['S', 'Sim'], ['N', 'Não']], default='N', max_length=1, verbose_name='7. O idoso se sente mais velho do que realmente é?'),
        ),
        migrations.AddField(
            model_name='negativeattitudesaging',
            name='q7_age_self_perception_why',
            field=models.TextField(blank=True, null=True, verbose_name='7. Por quê?'),
        ),
        migrations.AddField(
            model_name='negativeattitudesaging',
            name='q8_aging_analyse',
            field=models.CharField(choices=[['S', 'Sim'], ['N', 'Não']], default='N', max_length=1, verbose_name='8. É perceptível uma visão mais negativa da velhice? '),
        ),
        migrations.AddField(
            model_name='negativeattitudesaging',
            name='q8_aging_negative_points',
            field=models.ManyToManyField(blank=True, related_name='NegativePoints', to='page_section.AgingAspects', verbose_name='Aspectos positivos Envelhecimento'),
        ),
        migrations.AddField(
            model_name='negativeattitudesaging',
            name='q8_aging_positive_points',
            field=models.ManyToManyField(blank=True, related_name='PositivePoints', to='page_section.AgingAspects', verbose_name='Aspectos positivos Envelhecimento'),
        ),
        migrations.AlterField(
            model_name='cognitiondeficit',
            name='q1_memory_good_like_before',
            field=models.CharField(choices=[['S', 'Sim'], ['N', 'Não']], default='N', max_length=1, verbose_name='1. O(A) senhor(a) considera que sua memória é tão boa quanto antes?'),
        ),
        migrations.AlterField(
            model_name='cognitiondeficit',
            name='q2_memory_test',
            field=models.CharField(choices=[['S', 'Sim'], ['N', 'Não']], default='N', max_length=1, verbose_name='2.Memória'),
        ),
    ]
