from django.shortcuts import render
from datetime import timezone, datetime
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpRequest
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.db import models
from .forms import feedbackForm, CommentForm, CourseForm
from .models import Course,Comment


def index(request):
    return render(request,"course/index.html")
def partners(request):
    return render(request,"course/partners.html")
def feedback(request):
    data = None
    gender = {'1':'Мужской','2':'Женский'}
    job = {'1':'Обучаюсь',
        '2':'Обучаюсь и работаю',
        '3':'Работаю на полставки',
        '4':'Работаю полный день'}
    if request.method == 'POST':
        form = feedbackForm(request.POST)
        if form.is_valid():
            data = dict()
            data['name'] = form.cleaned_data['name']
            data['email'] = form.cleaned_data['email']
            data['gender'] = gender[form.cleaned_data['gender']]
            data['job'] = job[form.cleaned_data['job']]
            if(form.cleaned_data['notice'] == True):
                data['notice'] = 'Да'
            else:
                data['notice'] = 'Нет'
            data['message'] = form.cleaned_data['message']
            form = None
    else:
        form = feedbackForm()
    return render(request,'course/feedback.html',
    {
        'form':form,
        'data':data
    })
def registration(request):
    assert isinstance(request, HttpRequest)
    if request.method == "POST":
        regform = UserCreationForm (request.POST)
        if regform.is_valid():
            reg_f = regform.save(commit=False)
            reg_f.is_staff = False
            reg_f.is_active = True
            reg_f.is_superuser = False
            reg_f.date_joined = datetime.now()
            reg_f.last_login = datetime.now()
            reg_f.save()
            return redirect('index')
    else:
        regform = UserCreationForm()
    return render(
    request,
    'course/registration.html',
    {
    'regform': regform,
    'year':datetime.now().year,
    })
def courses(request):
    courses = Course.objects.all() #
    print(courses)
    return render(request,'course/courses.html',
    {
    'title':'Курс',
    'courses': courses,
    'year':datetime.now().year,
    }
    )
def course(request,id):
    course = Course.objects.get(pk=id)
    comments = Comment.objects.filter(post=id)
    print(course)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_f = form.save(commit=False)
            comment_f.author = request.user
            comment_f.date = datetime.now()
            comment_f.post = Course.objects.get(id=id)
            comment_f.save()
            return redirect('course', id=course.id)
    else:
        form = CommentForm()


    return render(request,'course/course.html',{
        'course':course,
        'comments':comments,
        'form':form,
        'year':datetime.now().year,
    })
def createCourse(request):
    if request.method == 'POST':
        courseform = CourseForm(request.POST,request.FILES)
        if courseform.is_valid():
            course_f = courseform.save(commit=False)
            course_f.posted = datetime.now()
            course_f.author = request.user
            course_f.save()

            return redirect('courses')
    else:
        courseform = CourseForm()

    return render(request,'course/createcourse.html',{
        'courseform':courseform,
        'title':'Добавить курс',
        'year':datetime.now().year,
    })
def videos(request):
    return render(request,'course/videos.html')