# Generated by Django 3.0.8 on 2021-06-23 16:57

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210619_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_assignments',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 23, 22, 27, 10, 785944)),
        ),
        migrations.CreateModel(
            name='submission',
            fields=[
                ('submission_id', models.AutoField(primary_key=True, serialize=False)),
                ('submission_date', models.DateTimeField(default=datetime.datetime(2021, 6, 23, 22, 27, 10, 787938))),
                ('submission_status', models.IntegerField()),
                ('assignment_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.student_assignments')),
                ('student_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.student_user')),
            ],
        ),
    ]
