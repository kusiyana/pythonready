from django.contrib.auth.models import User
from django.db import models
from tinymce.models import HTMLField
from datetime import datetime

class Course(models.Model):
    name = models.CharField(max_length=128)
    tutor =  models.ForeignKey(User, related_name='tutor',
        on_delete=models.CASCADE, null=True)
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
    video_link = models.CharField(max_length=200, blank=True)
    pdf_file = models.CharField(max_length=200, null=True)
    use_shell = models.IntegerField(default=0)                                  # 0 = false, 1 = True
    has_test = models.IntegerField(default=0)                                   # 0 = false, 1 = True
    created = models.DateTimeField(default=datetime.now)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']        

class Teststatus(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Test(models.Model):
    lecture = models.ForeignKey(Lecture, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    submission = models.CharField(max_length=1000, blank=True)
    teststatus = models.ForeignKey(Teststatus, on_delete=models.DO_NOTHING)
    mark_percent = models.IntegerField(default=0)
    examiner = models.ForeignKey(User, related_name='examiner', on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now=True)
    marked_date = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name
