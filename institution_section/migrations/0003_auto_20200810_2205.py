# Generated by Django 2.2.6 on 2020-08-10 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institution_section', '0002_auto_20200730_1241'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.AlterField(
            model_name='address',
            name='cep',
            field=models.CharField(max_length=9),
        ),
        migrations.AlterField(
            model_name='address',
            name='district',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='address',
            name='number',
            field=models.CharField(max_length=8),
        ),
    ]