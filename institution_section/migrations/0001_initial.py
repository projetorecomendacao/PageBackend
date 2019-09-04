# Generated by Django 2.2.4 on 2019-09-02 23:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=75)),
                ('number', models.IntegerField()),
                ('district', models.CharField(max_length=40)),
                ('cep', models.IntegerField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('communication', models.CharField(max_length=50)),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='institution', to='institution_section.Address')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Professional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('communication', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('professional_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='institution_section.Professional')),
                ('formation', models.CharField(max_length=45)),
            ],
            options={
                'ordering': ['id'],
            },
            bases=('institution_section.professional',),
        ),
        migrations.CreateModel(
            name='Responsible',
            fields=[
                ('professional_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='institution_section.Professional')),
            ],
            options={
                'ordering': ['id'],
            },
            bases=('institution_section.professional',),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('communication', models.CharField(max_length=50)),
                ('parking', models.CharField(max_length=50)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='locations', to='institution_section.Address')),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='locations', to='institution_section.Institution')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('professional_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='institution_section.Professional')),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='contacts', to='institution_section.Institution')),
                ('locations', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='contacts', to='institution_section.Location')),
            ],
            options={
                'ordering': ['id'],
            },
            bases=('institution_section.professional',),
        ),
    ]
