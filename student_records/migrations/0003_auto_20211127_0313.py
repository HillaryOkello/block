# Generated by Django 3.1.1 on 2021-11-27 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_records', '0002_auto_20211127_0309'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentrecord',
            name='AWS_practitioner_exams',
        ),
        migrations.RemoveField(
            model_name='studentrecord',
            name='aws_ml_exam',
        ),
        migrations.RemoveField(
            model_name='studentrecord',
            name='blockchain_exam',
        ),
        migrations.RemoveField(
            model_name='studentrecord',
            name='date_of_enrollment',
        ),
        migrations.RemoveField(
            model_name='studentrecord',
            name='date_of_graduation',
        ),
        migrations.RemoveField(
            model_name='studentrecord',
            name='dissertation_score',
        ),
        migrations.RemoveField(
            model_name='studentrecord',
            name='job_placement',
        ),
        migrations.RemoveField(
            model_name='studentrecord',
            name='python_associate_level_exam',
        ),
        migrations.RemoveField(
            model_name='studentrecord',
            name='python_entry_level',
        ),
        migrations.RemoveField(
            model_name='studentrecord',
            name='quiz_scores',
        ),
    ]
