from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('signin_student',views.signin_student,name='signin_student'),
    path('signin_teacher',views.signin_teacher,name='signin_teacher'),
    path('signup',views.signup,name='signup'),
    path('studentlanding_page',views.studentlanding_page,name='studentlanding_page'),
    path('teacherlanding_page',views.teacherlanding_page,name='teacherlanding_page'),
    path('course_dashboard',views.course_dashboard,name='course_dashboard'),
    path('opt_course',views.opt_course,name='opt_course'),
    path('student_detail',views.student_detail,name='student_detail'),
    path('student_attendance',views.student_attendance,name='student_attendance'),
    path('update_attendance',views.update_attendance,name='update_attendance'),
    path('update_marks',views.update_marks,name='update_marks'),
    path('student_marks',views.student_marks,name='student_marks'),
    path('teacher_course_details',views.teacher_course_details,name='teacher_course_details'),
    path('create_announcement',views.create_announcement,name='create_announcement'),
    path('about_us',views.about_us,name='about_us'),
    path('logout_viewsstudent',views.logout_viewsstudent,name='logout_viewsstudent'),
    path('logout_viewsteacher',views.logout_viewsteacher,name='logout_viewsteacher'),
    # path('view_specific_announcements',views.view_specific_announcements,name='view_specific_announcements'),
    # path('announce',views.announce,name='announce'),
    
]