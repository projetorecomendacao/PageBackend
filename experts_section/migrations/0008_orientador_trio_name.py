# Generated by Django 3.0.7 on 2020-11-30 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experts_section', '0007_orientador_qtdpages'),
    ]

    operations = [
        migrations.AddField(
            model_name='orientador',
            name='trio_name',
            field=models.CharField(blank=True, max_length=60),
        ),
    ]
