from django.contrib import admin
from .models import Details,Course,StudentCourse, Teacher, Announcement, StudentSection

# Register your models here.
admin.site.register(Details)
admin.site.register(StudentCourse)
admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(Announcement)
admin.site.register(StudentSection)




