# Generated by Django 4.2.20 on 2025-03-31 11:28

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['-posted'], 'verbose_name': 'Курс', 'verbose_name_plural': 'Курсы'},
        ),
        migrations.AlterField(
            model_name='course',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2025, 3, 31, 14, 28, 1, 92127), verbose_name='Дата добавления курса'),
        ),
        migrations.AlterModelTable(
            name='course',
            table='Course',
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст комментария')),
                ('date', models.DateTimeField(db_index=True, default=datetime.datetime(2025, 3, 31, 14, 28, 1, 93215), verbose_name='Дата комментария')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор комментария')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course', verbose_name='Статья комментария')),
            ],
            options={
                'verbose_name': 'Комментарий к статье блога',
                'verbose_name_plural': 'Комментарии к статье блога',
                'db_table': 'Comment',
                'ordering': ['-date'],
            },
        ),
    ]
