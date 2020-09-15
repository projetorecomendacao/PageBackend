# Generated by Django 2.2.6 on 2020-09-03 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('page_section', '0004_auto_20200903_1955'),
        ('recommender_section', '0002_auto_20200818_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommendedactivities',
            name='page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='page5', to='page_section.Page', verbose_name='PAGe'),
        ),
        migrations.AddField(
            model_name='recommendedactivitiesoffers',
            name='page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='page4', to='page_section.Page', verbose_name='PAGe'),
        ),
    ]
