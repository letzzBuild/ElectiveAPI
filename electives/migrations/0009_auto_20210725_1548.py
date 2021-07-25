# Generated by Django 3.1.7 on 2021-07-25 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_students_cgpa'),
        ('electives', '0008_auto_20210723_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='electivedetails',
            name='elective_id',
            field=models.ForeignKey(db_column='elective_id', on_delete=django.db.models.deletion.CASCADE, to='electives.electives'),
        ),
        migrations.CreateModel(
            name='ElectiveChoosenPriority',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('elective_name', models.CharField(max_length=40)),
                ('priority', models.IntegerField()),
                ('student_id', models.ForeignKey(db_column='student_id', on_delete=django.db.models.deletion.CASCADE, to='students.students')),
            ],
            options={
                'db_table': 'elective_priority_selected',
            },
        ),
    ]
