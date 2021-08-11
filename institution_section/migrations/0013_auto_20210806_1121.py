# Generated by Django 3.1.6 on 2021-08-06 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('institution_section', '0012_auto_20201119_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='LegalNature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=40, null=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='PeopleIncapacity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=140, null=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='PeopleRangeAge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=40, null=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='PeopleSex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=40, null=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='PeopleType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=40, null=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.RemoveField(
            model_name='targetaudience',
            name='most_people_served_incapacity',
        ),
        migrations.RemoveField(
            model_name='targetaudience',
            name='most_people_served_range_age',
        ),
        migrations.RemoveField(
            model_name='targetaudience',
            name='most_people_served_sex',
        ),
        migrations.RemoveField(
            model_name='targetaudience',
            name='most_people_served_type',
        ),
        migrations.RemoveField(
            model_name='targetaudience',
            name='people_can_be_served',
        ),
        migrations.AddField(
            model_name='institution',
            name='emailMain',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='institution',
            name='facebook',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='institution',
            name='instagram',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='institution',
            name='phoneMain',
            field=models.CharField(blank=True, max_length=14, null=True),
        ),
        migrations.AddField(
            model_name='institution',
            name='phoneWhatsapp',
            field=models.CharField(blank=True, max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='offers',
            name='capacity',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='institution_section.capacity'),
        ),
        migrations.AlterField(
            model_name='offers',
            name='comments',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='offers',
            name='date_begin',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='offers',
            name='date_end',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='offers',
            name='motivation',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='offers',
            name='requisites',
            field=models.TextField(null=True),
        ),
    ]
