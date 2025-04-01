from django.db import models
from django.contrib import admin
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import User

class Course(models.Model):
    title = models.CharField(max_length=100, unique_for_date="posted",verbose_name="Название курса")
    description = models.TextField(verbose_name="Краткое содержание")
    content = models.TextField(verbose_name="Содержание")
    #image = models.ImageField(upload_to="course/static/course/content/coursesImages", verbose_name="Иконка курса", null=True, blank=True)
    image_path = models.FileField(default="temp.jpg", verbose_name="Путь к картинке",null=True, blank=True)
    posted = models.DateTimeField(default = datetime.now(), db_index = True,verbose_name="Дата добавления курса")
    teacher = models.ForeignKey(User,null=True, blank=True, on_delete=models.RESTRICT, verbose_name="Преподаватель")

    def get_absolute_url(self):
        return reverse("blogpost",args=[str(self.id)])
    def __str__(self):
        return self.title

    class Meta:
        db_table = "Course"
        ordering = ["-posted"]
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

class Comment(models.Model):
    text = models.TextField(verbose_name="Текст комментария")
    date = models.DateTimeField(default = datetime.now(),db_index=True,verbose_name="Дата комментария")
    author = models.ForeignKey(User, on_delete= models.CASCADE, verbose_name="Автор комментария")
    post = models.ForeignKey(Course,on_delete=models.CASCADE,verbose_name="Статья комментария")

    def __str__(self):
        return 'Комментарий к %d %s к %s' % (self.id,self.author,self.post)
    class Meta:
        db_table = "Comment"
        ordering = ["-date"]
        verbose_name = "Комментарий к статье блога"
        verbose_name_plural = "Комментарии к статье блога"
