# Generated by Django 2.2.6 on 2021-03-17 11:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campus', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='student_id',
            new_name='student_name',
        ),
        migrations.AlterField(
            model_name='faculties',
            name='dob',
            field=models.DateField(default=datetime.datetime(2021, 3, 17, 16, 58, 58, 141526)),
        ),
        migrations.AlterField(
            model_name='project',
            name='rating_star',
            field=models.CharField(default='0', max_length=3),
        ),
    ]