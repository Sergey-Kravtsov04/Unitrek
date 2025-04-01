from datetime import datetime
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('partners', views.partners, name='partners'),
    path('feedback', views.feedback, name='feedback'),
    path('registration', views.registration, name='registration'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
    path('login/',LoginView.as_view(
             template_name='course/login.html',
             extra_context={
             'year':datetime.now().year,
             }),
            name='login'),
    path('courses', views.courses, name='courses'),
    path('course/<int:id>/', views.course, name='course'),
    path('createCourse/', views.createCourse, name='createCourse'),
    path('videos/', views.videos, name='videos'),
]
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns+= staticfiles_urlpatterns()
