# Generated by Django 3.1.6 on 2021-05-21 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('esm_program_section', '0028_auto_20210415_1243'),
        ('editor_psicometrico', '0002_documento_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActionsEditor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actionType', models.CharField(default='c', max_length=1)),
                ('objectType', models.CharField(default='1', max_length=1)),
                ('documento_id', models.IntegerField(blank=True, default=-1, null=True)),
                ('dimensao_id', models.IntegerField(blank=True, default=-1, null=True)),
                ('dominio_id', models.IntegerField(blank=True, default=-1, null=True)),
                ('questao_id', models.IntegerField(blank=True, default=-1, null=True)),
                ('anterior', models.JSONField(blank=True, null=True)),
                ('actionDate', models.CharField(blank=True, max_length=50, null=True)),
                ('createDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('editor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='esm_program_section.editorprogram')),
            ],
        ),
    ]
