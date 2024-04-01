from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=10, unique=True)
    dept = models.CharField(max_length=50)

    def __str__(self):
        return self.course_code
    
class Details(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    regno = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    gender = models.CharField(max_length=10)
    contact_number = models.CharField(max_length=15)
    branch = models.CharField(max_length=100)
   
    
    def __str__(self):
        return self.regno
    



class StudentCourse(models.Model):
    regno = models.ForeignKey(Details, on_delete=models.CASCADE)
    course_code = models.ForeignKey(Course, on_delete=models.CASCADE)
    attendance = models.FloatField(default=0)  # Assuming it's a percentage
    course_marks = models.FloatField(default=0)  # Assuming it's a numeric value

    def __str__(self):
        return f"Reg No: {self.regno}, Course Code: {self.course_code}"
    
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    regno = models.ForeignKey('Details', on_delete=models.CASCADE)
    course_code = models.ForeignKey('Course', on_delete=models.CASCADE)
    section = models.CharField(max_length=10)  # Assuming section is a string identifier

    def __str__(self):
        return f"Teacher: {self.user.username}, Course: {self.course_code.course_name}, Section: {self.section}"

class Announcement(models.Model):
    regno = models.ForeignKey('Details', on_delete=models.CASCADE)
    message = models.TextField()
    section = models.CharField(max_length=50, blank=True, null=True)
    def __str__(self):
        return f"Announcement from {self.regno.user.username}"

class StudentSection(models.Model):
    regno = models.ForeignKey('Details', on_delete=models.CASCADE)
    section = models.CharField(max_length=10)  # Assuming section is a string identifier

    def __str__(self):
        return f"Student: {self.regno.user.username}, Section: {self.section}"