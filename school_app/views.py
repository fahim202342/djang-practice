from urllib import request

from django.shortcuts import redirect, render

from school_app.models import CourseModel, DepartmentModel, StudentModel, TeacherModel

def home(request):
    return render(request, 'home.html')

def teacher(request):
    teachers = TeacherModel.objects.all()
    context = {
        'teachers': teachers
    }
    return render(request, 'teacher.html', context=context)

def add_teacher(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        email = request.POST.get('email')
        
        TeacherModel.objects.create(
            name = name,
            address = address,
            email = email
        )
        
        return redirect('teacher')
        
    return render(request, 'add-teacher.html')
    

def student(request):
    
    students = StudentModel.objects.all()
    context = {
        'students': students
    }
    return render(request, 'student.html', context=context)

def department(request):
    
    department = DepartmentModel.objects.all()
    context = {
        'department' : department
    }
    
    return render(request, 'department.html', context=context)

def course(request):
    course = CourseModel.objects.all()
    context = {
        'course' : course
    }
    
    return render(request, 'course.html', context=context)
    