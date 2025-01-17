# Generated by Django 3.0.8 on 2021-06-16 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course_list',
            name='course_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='course_list',
            name='teacher_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.teacher_user'),
        ),
    ]
