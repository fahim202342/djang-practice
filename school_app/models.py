from django.db import models

# Create your models here.
class TeacherModel(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    
    
class StudentModel(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    
class DepartmentModel(models.Model):
    name = models.CharField(max_length=100)
    head = models.CharField(max_length=100)
    office_number = models.IntegerField(blank=True,null=True)   
    
class CourseModel(models.Model):
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    credit = models.IntegerField()    
 
