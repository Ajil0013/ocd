from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime

# Create your models here.
class all_users(models.Model):
    username = models.CharField(max_length=100, primary_key=True)
    user_type = models.BooleanField(default=False)


class teacher_user(models.Model):
    first_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    last_name = models.CharField(max_length=100)
    # username = models.ForeignKey(all_users, primary_key=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, primary_key=True)


class student_user(models.Model):
    first_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    last_name = models.CharField(max_length=100)
    # username = models.ForeignKey(all_users, primary_key=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, primary_key=True)


class course_list(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=200, blank=False)
    teacher_id = models.ForeignKey(teacher_user, null=True, on_delete=models.SET_NULL)


class student_assignments(models.Model):
    assignment_id = models.AutoField(primary_key=True)
    course_id = models.ForeignKey(course_list, on_delete=models.CASCADE)
    assignment_name = models.TextField(blank=True, null=True)
    assignment_body = models.TextField(blank=True, null=True)
    published_date = models.DateTimeField(default=datetime.now())
    due_date = models.DateTimeField()
    status = models.IntegerField()
    #status_dict::{'draft':0, 'posted':1, 'submitted':2, 'overdue':3, 'discarded':4}


class student_course_bridge(models.Model):
    course_id = models.ForeignKey(course_list, on_delete=models.CASCADE)
    student_id = models.ForeignKey(student_user, on_delete = models.CASCADE)


class submission(models.Model):
    submission_id = models.AutoField(primary_key=True)
    assignment_id = models.ForeignKey(student_assignments, null = True, on_delete=models.SET_NULL)
    student_id = models.ForeignKey(student_user, null=True, on_delete=models.SET_NULL)
    submission_date = models.DateTimeField(default=datetime.now())
    submission_status = models.IntegerField()
    submission_code = models.TextField(blank=True, null=True)
    submission_lang = models.CharField(max_length=150, blank=True, null=True)
    #submission_status_dict::{'not_submitted': 0, 'submitted':1, 'redo':2}