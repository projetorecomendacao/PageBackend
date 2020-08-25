# Generated by Django 3.0.7 on 2020-08-18 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activities_section', '0001_initial'),
        ('institution_section', '0003_auto_20200810_2205'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicEducation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ActingTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeActing', models.IntegerField(default=0)),
                ('historic', models.TextField(null=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='AssistanceModality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Capacity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CAD', models.IntegerField(null=True)),
                ('CAD_M', models.IntegerField(null=True)),
                ('CAD_F', models.IntegerField(null=True)),
                ('CAP', models.IntegerField(null=True)),
                ('CAP_M', models.IntegerField(null=True)),
                ('CAP_F', models.IntegerField(null=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ContactMeans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('phone', models.CharField(max_length=14)),
                ('mobilePhone', models.CharField(max_length=14)),
                ('fax', models.CharField(max_length=14)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ExpertiseAreas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Locals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('objective', models.TextField(null=True)),
                ('targetAudience', models.TextField(max_length=50, null=True)),
                ('ageTargetAudience', models.TextField(max_length=50, null=True)),
                ('comments', models.TextField(null=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='LongaDuracao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='institution_section.Capacity')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='WebAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('webPage', models.CharField(max_length=100)),
                ('facebook', models.CharField(max_length=100)),
                ('instagram', models.CharField(max_length=100)),
                ('tweeter', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.RemoveField(
            model_name='instructor',
            name='professional_ptr',
        ),
        migrations.RemoveField(
            model_name='location',
            name='address',
        ),
        migrations.RemoveField(
            model_name='location',
            name='institution',
        ),
        migrations.RemoveField(
            model_name='responsible',
            name='professional_ptr',
        ),
        migrations.AlterModelOptions(
            name='offers',
            options={'ordering': ['id']},
        ),
        migrations.RenameField(
            model_name='institution',
            old_name='communication',
            new_name='comments',
        ),
        migrations.RemoveField(
            model_name='institution',
            name='email',
        ),
        migrations.RemoveField(
            model_name='institution',
            name='name',
        ),
        migrations.RemoveField(
            model_name='institution',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='offers',
            name='activitie',
        ),
        migrations.RemoveField(
            model_name='offers',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='offers',
            name='instructor',
        ),
        migrations.RemoveField(
            model_name='offers',
            name='responsible',
        ),
        migrations.RemoveField(
            model_name='professional',
            name='communication',
        ),
        migrations.AddField(
            model_name='address',
            name='cidade',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='institution_section.Cidade'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cidade',
            name='country',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cidade',
            name='name',
            field=models.CharField(default='City', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cidade',
            name='state',
            field=models.CharField(default='Sao Paulo', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='institution',
            name='CNPJ',
            field=models.TextField(max_length=17, null=True),
        ),
        migrations.AddField(
            model_name='institution',
            name='ageTargetAudience',
            field=models.TextField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='institution',
            name='companyFancyName',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='institution',
            name='companyName',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='institution',
            name='objective',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='institution',
            name='targetAudience',
            field=models.TextField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='offers',
            name='activities',
            field=models.ManyToManyField(to='activities_section.Activity'),
        ),
        migrations.AddField(
            model_name='offers',
            name='comments',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offers',
            name='instructors',
            field=models.ManyToManyField(related_name='_instructors', to='institution_section.Professional'),
        ),
        migrations.AddField(
            model_name='offers',
            name='responsibles',
            field=models.ManyToManyField(related_name='_responsibles', to='institution_section.Professional'),
        ),
        migrations.AddField(
            model_name='professional',
            name='CPF',
            field=models.CharField(default='', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='professional',
            name='RG',
            field=models.CharField(default='', max_length=12),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='institution',
            name='address',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='institution_section.Address'),
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.DeleteModel(
            name='Instructor',
        ),
        migrations.DeleteModel(
            name='Responsible',
        ),
        migrations.AddField(
            model_name='locals',
            name='address',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='institution_section.Address'),
        ),
        migrations.AddField(
            model_name='locals',
            name='contactMeans',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='institution_section.ContactMeans'),
        ),
        migrations.AddField(
            model_name='locals',
            name='technicalResponsible',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='institution_section.Professional'),
        ),
        migrations.AddField(
            model_name='locals',
            name='webAddress',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='institution_section.WebAddress'),
        ),
        migrations.AddField(
            model_name='actingtime',
            name='assistenceModality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institution_section.AssistanceModality'),
        ),
        migrations.AddField(
            model_name='actingtime',
            name='institution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institution_section.Institution'),
        ),
        migrations.AddField(
            model_name='institution',
            name='assitence',
            field=models.ManyToManyField(through='institution_section.ActingTime', to='institution_section.AssistanceModality'),
        ),
        migrations.AddField(
            model_name='institution',
            name='contactMeans',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='institution_section.ContactMeans'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='institution',
            name='webAddress',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='institution_section.WebAddress'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offers',
            name='capacity',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='institution_section.Capacity'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='professional',
            name='academicEducation',
            field=models.ManyToManyField(to='institution_section.AcademicEducation'),
        ),
        migrations.AddField(
            model_name='professional',
            name='contactMeans',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='institution_section.ContactMeans'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='professional',
            name='expertiseAreas',
            field=models.ManyToManyField(to='institution_section.ExpertiseAreas'),
        ),
        migrations.AddField(
            model_name='professional',
            name='webAddress',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='institution_section.WebAddress'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='offers',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='institution_section.Locals'),
        ),
    ]
