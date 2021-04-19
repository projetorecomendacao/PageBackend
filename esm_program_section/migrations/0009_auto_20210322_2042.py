# Generated by Django 3.1.6 on 2021-03-22 20:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('esm_program_section', '0008_auto_20210322_2038'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='program',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='esm_program_section.program'),
        ),
        migrations.AlterField(
            model_name='actionsesm',
            name='actionDate',
            field=models.CharField(blank=True, default='1616445752000', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='program',
            name='updateDate',
            field=models.CharField(blank=True, default='1616445752000', max_length=50),
        ),
    ]