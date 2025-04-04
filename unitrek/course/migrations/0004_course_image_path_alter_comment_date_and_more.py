# Generated by Django 4.2.20 on 2025-03-31 16:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_alter_comment_date_alter_course_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image_path',
            field=models.FileField(blank=True, null=True, upload_to='temp.jpg', verbose_name='Путь к картинке'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2025, 3, 31, 19, 14, 30, 588130), verbose_name='Дата комментария'),
        ),
        migrations.AlterField(
            model_name='course',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2025, 3, 31, 19, 14, 30, 587596), verbose_name='Дата добавления курса'),
        ),
    ]
