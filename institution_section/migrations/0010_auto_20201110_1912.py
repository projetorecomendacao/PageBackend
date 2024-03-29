# Generated by Django 2.2.6 on 2020-11-10 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('institution_section', '0009_auto_20201020_1312'),
    ]

    operations = [
        migrations.CreateModel(
            name='TargetAudience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(null=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.RenameField(
            model_name='institution',
            old_name='assitence',
            new_name='assitenceModality',
        ),
        migrations.RenameField(
            model_name='institution',
            old_name='comments',
            new_name='schedules',
        ),
        migrations.RenameField(
            model_name='locals',
            old_name='comments',
            new_name='parkingDescription',
        ),
        migrations.RemoveField(
            model_name='institution',
            name='ageTargetAudience',
        ),
        migrations.RemoveField(
            model_name='locals',
            name='ageTargetAudience',
        ),
        migrations.RemoveField(
            model_name='locals',
            name='technicalResponsible',
        ),
        migrations.RemoveField(
            model_name='offers',
            name='active_aging',
        ),
        migrations.RemoveField(
            model_name='offers',
            name='ambience',
        ),
        migrations.RemoveField(
            model_name='offers',
            name='genre_goals',
        ),
        migrations.RemoveField(
            model_name='offers',
            name='loe_income',
        ),
        migrations.RemoveField(
            model_name='offers',
            name='people_class',
        ),
        migrations.RemoveField(
            model_name='typedigitaladdress',
            name='name',
        ),
        migrations.AddField(
            model_name='institution',
            name='category',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='institution',
            name='foundedIn',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='institution',
            name='legalKind',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='locals',
            name='haveParking',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='locals',
            name='schedules',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='offers',
            name='continuosFlow',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='offers',
            name='enrollmentOpen',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='offers',
            name='environmentType',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='offers',
            name='exemption',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='offers',
            name='healthyAging',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='offers',
            name='specificObjectives',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='typedigitaladdress',
            name='description',
            field=models.CharField(default='a', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='institution',
            name='targetAudience',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='institution_section.TargetAudience'),
        ),
        migrations.AlterField(
            model_name='locals',
            name='targetAudience',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='institution_section.TargetAudience'),
        ),
        migrations.AlterField(
            model_name='offers',
            name='schedule',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='typedigitaladdress',
            name='type',
            field=models.CharField(max_length=40),
        ),
        migrations.AddField(
            model_name='offers',
            name='targetAudience',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='institution_section.TargetAudience'),
        ),
    ]
