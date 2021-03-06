# Generated by Django 3.2 on 2021-06-17 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0003_faculty_faculty_name'),
        ('students', '0003_students_usn'),
        ('electives', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='electivesemester',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='ElectiveDetails',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('total_intake', models.IntegerField()),
                ('scope', models.TextField()),
                ('syllabus_pdf', models.TextField()),
                ('company_names', models.TextField()),
                ('introduction_video', models.TextField()),
                ('elective_id', models.ForeignKey(db_column='elective_id', on_delete=django.db.models.deletion.CASCADE, to='electives.electives')),
            ],
        ),
        migrations.CreateModel(
            name='ElectiveStudent',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('elective_id', models.ForeignKey(db_column='elective_id', on_delete=django.db.models.deletion.CASCADE, to='electives.electives')),
                ('student_id', models.ForeignKey(db_column='student_id', on_delete=django.db.models.deletion.CASCADE, to='students.students')),
            ],
            options={
                'verbose_name_plural': 'student_electives',
                'db_table': 'student_electives',
                'unique_together': {('elective_id', 'student_id')},
            },
        ),
        migrations.CreateModel(
            name='ElectiveFaculty',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('elective_id', models.ForeignKey(db_column='elective_id', on_delete=django.db.models.deletion.CASCADE, to='electives.electives')),
                ('faculty_id', models.ForeignKey(db_column='faculty_id', on_delete=django.db.models.deletion.CASCADE, to='faculty.faculty')),
            ],
            options={
                'verbose_name_plural': 'faculty_electives',
                'db_table': 'faculty_electives',
                'unique_together': {('elective_id', 'faculty_id')},
            },
        ),
    ]
