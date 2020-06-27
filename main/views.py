from django.shortcuts import render, redirect
from .models import Course, Lecture, Section
from django.contrib.auth.models import User

def index(request):
    """
    Main page functionality
    """

    start_course_id = 1
    sections = Section.objects.filter(course_id=start_course_id)
    course = Course.objects.get(pk=start_course_id)
    section_lectures, lecture_counts = {}, {}
    for section in sections:
        section_lectures[section.name] = Lecture.objects.filter(section_id=section.id)
        lecture_counts[section.name] = len(section_lectures[section.name])
    context_dict = {
        'page_title': "Home"
        ,'course': course
        ,'section_lectures': section_lectures
        ,'lecture_counts': lecture_counts
        }
    return render(request, 'main/index.html', context_dict)

def view_lecture(request, lecture_number=""):
    """
    Main page functionality
    """
    if not lecture_number:
        return redirect('/')

    try:
        lecture = Lecture.objects.get(order=lecture_number)
    except:
        return redirect('/')
    lecture.poster = "".join([lecture.video_link[:-3], 'png'])
    context_dict = {
        'page_title': "View lecture"
        ,'lecture': lecture
        ,'next_lecture': lecture.order+1
        ,'previous_lecture': lecture.order-1
        }
    return render(request, 'main/view_lecture.html', context_dict)
