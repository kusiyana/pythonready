from django.contrib.auth.models import User
from django.db import models
from tinymce.models import HTMLField
from datetime import datetime

class Course(models.Model):
    name = models.CharField(max_length=128)
    tutor =  models.ForeignKey(User, related_name='tutor', on_delete=models.CASCADE, null=True)
    description = HTMLField()
    created = models.DateTimeField(default=datetime.now)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Section(models.Model):
    course_id = models.IntegerField()
    name = models.CharField(max_length=128)
    def __str__(self):
        return self.name


class Lecture(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    order = models.IntegerField(unique=True)
    name = models.CharField(max_length=128)
    content = HTMLField()
    video_link = models.CharField(max_length=200, null=True)
    extra_link = models.CharField(max_length=200, null=True)
    created = models.DateTimeField(default=datetime.now)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Create your models here.
