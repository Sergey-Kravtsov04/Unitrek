# Generated by Django 4.2.20 on 2025-03-31 17:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_course_image_path_alter_comment_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2025, 3, 31, 20, 7, 13, 274023), verbose_name='Дата комментария'),
        ),
        migrations.AlterField(
            model_name='course',
            name='image_path',
            field=models.FileField(blank=True, default='temp.jpg', null=True, upload_to='', verbose_name='Путь к картинке'),
        ),
        migrations.AlterField(
            model_name='course',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2025, 3, 31, 20, 7, 13, 273546), verbose_name='Дата добавления курса'),
        ),
    ]
