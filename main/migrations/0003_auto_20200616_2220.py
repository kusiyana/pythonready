# Generated by Django 3.0.5 on 2020-06-16 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_course_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='section',
            old_name='lecture_id',
            new_name='course_id',
        ),
    ]