# Generated by Django 3.1.1 on 2021-11-27 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_records', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentrecord',
            name='date_of_enrollment',
            field=models.DateField(default='11/11/1111', max_length=50),
        ),
        migrations.AlterField(
            model_name='studentrecord',
            name='date_of_graduation',
            field=models.DateField(default='11/11/1111', max_length=50),
        ),
        migrations.AlterField(
            model_name='studentrecord',
            name='dob',
            field=models.DateField(default='11/11/1111', max_length=50),
        ),
    ]
