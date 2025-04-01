from django import forms
from django.db import models
from .models import Comment,Course

class feedbackForm(forms.Form):
    name = forms.CharField(label='Ваше имя', min_length=2, max_length=100, widget=forms.TextInput(attrs={'class': 'w-100'}))
    email = forms.EmailField(label='Ваш e-mail', min_length=5, widget=forms.TextInput(attrs={'class': 'w-100'}))
    gender = forms.ChoiceField(label='Ваш пол', choices=[
        ('1', 'Мужской'),
        ('2', 'Женский')
    ],
        widget= forms.RadioSelect, initial=1)
    job = forms.ChoiceField(label='Тип занятости', choices=[
        ('1','Обучаюсь'),
        ('2','Обучаюсь и работаю'),
        ('3','Работаю на полставки'),
        ('4','Работаю полный день'),
    ],
        initial=1)
    notice = forms.BooleanField(label='Получать новости о разработке сайта', required=False)
    message = forms.CharField(label='Чтобы вы улучшили в работе сайта',
                              widget=forms.Textarea(attrs={
                                  'rows':5,
                                  'cols':50,
                                  'class': 'w-100',
                              }))

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {'text':''}

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title','description','content','image_path',)
        labels = {'title':'Заголовок','description':'Краткое содержание','content':'Полное содержание','image_path':'Изображение'}
