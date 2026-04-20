from django.contrib import admin
from django.urls import path,include
from .views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('teachers/', teacher, name='teacher'),
    path('students/', student, name='student'),
    path('department/', department, name='department'),
    path('course/', course, name='course'),
    path('add-teachers/', add_teacher, name='add-teacher'),
]
