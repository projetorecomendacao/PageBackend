# Generated by Django 2.2.6 on 2020-02-14 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=30)),
                ('measure', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='IngestedDrinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('drink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drinks_section.Drinks')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
