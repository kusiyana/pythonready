from django.contrib import admin

# Register your models here.
from .models import Course, Lecture, Section
admin.site.register(Course)
admin.site.register(Lecture)
admin.site.register(Section)
