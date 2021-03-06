# Generated by Django 3.1.7 on 2021-06-14 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('branches', '0001_initial'),
        ('semesters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('student_id', models.AutoField(primary_key=True, serialize=False)),
                ('student_name', models.CharField(max_length=50)),
                ('branch_id', models.ForeignKey(db_column='branch_id', on_delete=django.db.models.deletion.CASCADE, to='branches.branches')),
                ('semester_id', models.ForeignKey(db_column='semester_id', on_delete=django.db.models.deletion.CASCADE, to='semesters.semesters')),
            ],
            options={
                'verbose_name_plural': 'students',
                'db_table': 'students',
            },
        ),
    ]
