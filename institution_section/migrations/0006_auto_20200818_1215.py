# Generated by Django 3.0.7 on 2020-08-18 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('institution_section', '0005_delete_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='cidade',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='institution_section.Cidade'),
        ),
        migrations.AlterField(
            model_name='cidade',
            name='country',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='cidade',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='cidade',
            name='state',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='professional',
            name='CPF',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='professional',
            name='RG',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='professional',
            name='contactMeans',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='institution_section.ContactMeans'),
        ),
        migrations.AlterField(
            model_name='professional',
            name='webAddress',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='institution_section.WebAddress'),
        ),
    ]
