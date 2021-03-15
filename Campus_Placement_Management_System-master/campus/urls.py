from django.urls import path,include
from django.conf.urls import url
# from .views import (
# 	StudentDashboardView,
# 	StudentExamView,
# 	StudentTimetableView,
# 	StudentProjectView,
# 	StudentAssignmentView,
# 	StudentAchievementView,
# 	StudentMaterialView,
# 	FacultyDashboardView,
# 	FacultyProfileView,
# 	FacultyMarksView,
# 	FacultyMaterialsView,
# 	FacultyStudentDataView,
# 	FacultyAssignmentView,
# 	FacultyViewAssignmentView,
#     AdminAddAdminView,
#     AdminCompanyView,
#     AdminFacultyView,
#     AdminStudentView,
#     AdminLoginView,
#     AdminLogoutView,
#     # initial_login,
#     StudentProfileView,



# )

# from .views import



# from .views import college,c_admin,faculty,student

from .views.c_admin import (AdminForgetPassView,AdminLogoutView,AdminLoginView,AdminStudentView, AdminFacultyView, AdminAddAdminView,AdminCompanyView)

from .views.student import (shome,StudentCertificateView,StudentForgetPassView,StudentLogoutView,StudentLoginView,StudentProfileView, StudentDashboardView,StudentLoginView,StudentAchievementView,StudentExamView,StudentProjectView,StudentEventView,Studentproject)

from .views.faculty import (FacultyForgetPassView,FacultyLogoutView,FacultyLoginView,FacultyDashboardView,FacultyProfileView,FacultyEventView,FacultyAddEventView)

from .views.college import (home,LogoutView,ForgetPasswordView,ActivateView,ChangePasswordView)

from django.contrib.auth import views as auth_views
app_name = 'campus'

urlpatterns = [
    # path('/',shome,name="initial_login"),
    path('login/',home,name="login"),
    # url(r'login/',home,name="login"),
    # path('',college.home,name="home"),
    # path('students/', include(([
    #     # path('', student.StudentLoginView, name='student_login'),
    #     # path('logout/',student.StudentLogoutView,name='student_logout'),
    #     # path('login/', student.StudentLoginView, name='student_login'),
    #     path('index/', student.StudentDashboardView, name='student_dashboard'),
    #     path('events/', student.StudentEventView, name='student_event'),
    #     path('achievements/', student.StudentAchievementView, name='student_achievements'),
    #     path('exams/', student.StudentExamView, name='student_exams'),
    #     path('projects/', student.StudentProjectView, name='student_projects'),
    #     path('profile/', student.StudentProfileView, name='student_profile'),
        
    # ], 'campus'), namespace='students')),



    # path('faculty/', include(([
    #     # path('', faculty.FacultyLoginView, name='faculty_login'),
    #     # path('logout/',faculty.FacultyLogoutView,name='faculty_logout'),
    #     # path('login/', faculty.FacultyLoginView, name='faculty_login'),
    #     path('index/', faculty.FacultyDashboardView.as_view(), name='faculty_dashboard'),
    #     path('events/', faculty.FacultyEventView.as_view(), name='faculty_events'),
    #     path('add_event/', faculty.FacultyAddEventView.as_view(), name='faculty_add_events'),
    #     path('profile/', faculty.FacultyProfileView.as_view(), name='faculty_profile'), 
    # ], 'campus'), namespace='faculties')),


    # path('c_admin/', include(([
    #     # path('', c_admin.AdminLoginView, name='admin_login'),
    #     # path('logout/',AdminLogoutView,name='admin_logout'),
    #     path('login/', c_admin.AdminLoginView, name='admin_login'),
    #     path('add_admin/', c_admin.AdminAddAdminView, name='admin_add_admin'),
    #     path('add_company/', c_admin.AdminCompanyView, name='admin_add_company'),
    #     path('add_faculty/', c_admin.AdminFacultyView, name='admin_add_faculty'),
    #     path('add_student/', c_admin.AdminStudentView, name='admin_add_student'), 
    # ], 'campus'), namespace='c_admin')),
    # path('/',initial_login,name='login_init'),
    # url(r'^login/$', auth_views.login ,{'template_name': 'C_Admin/login.html'}, name='login'),
    # path('students/profile', student.StudentProfileView, name="student_profile"),
    # path('students/', student.StudentDashboardView, name='student_dashboard'),
    # path('students/index', student.StudentDashboardView, name='student_dashboard'),
    # path('students/exams', student.StudentExamView, name='student_exams'),
    # # path('students/assignments', StudentAssignmentView, name='student_assignments'),
    # path('students/projects', student.StudentProjectView, name='student_projects'),
    # # path('students/timetable', StudentTimetableView, name='student_timetable'),
    # path('students/achievements', student.StudentAchievementView, name='student_achievements'),
    
    path('students/login',StudentLoginView,name="student_login"),
    path('students/profile', StudentProfileView, name="student_profile"),
    path('students/', StudentDashboardView, name='student_dashboard'),
    path('students/index', StudentDashboardView, name='student_dashboard'),
    path('students/exams', StudentExamView, name='student_exams'),
    path('students/certificate', StudentCertificateView, name='student_cerificate'),
    # path('students/assignments', StudentAssignmentView, name='student_assignments'),
    path('students/add_projects', StudentProjectView, name='student_projects'),
    path('students/projects', Studentproject, name='student_add_projects'),
    # path('students/timetable', StudentTimetableView, name='student_timetable'),
    path('students/achievements', StudentAchievementView, name='student_achievements'),
    
    path('students/certi', StudentCertificateView, name='student_achievements'),
    path('students/logout', StudentLogoutView, name='student_logout'),
    path('students/forgetPassword', StudentForgetPassView, name='student_forget'),
    # path('students/materials', StudentMaterialView, name='student_materials'),
    path('faculty/login',FacultyLoginView,name="faculty_login"),
    path('faculty/', FacultyDashboardView, name='faculty_dashboard'),
    path('faculty/index', FacultyDashboardView, name='faculty_dashboard'),
    path('faculty/profile', FacultyProfileView, name='faculty_profile'),
    path('faculty/add_event', FacultyAddEventView, name='faculty_add_event'),
    path('faculty/events', FacultyEventView, name='faculty_events'),
    path('faculty/logout', FacultyLogoutView, name='faculty_logout'),
    path('faculty/forgetPassword', FacultyForgetPassView, name='faculty_forget'),
    # path('faculty/materials', FacultyMaterialsView, name='faculty_material'),
    # path('faculty/view_Marks', FacultyMarksView, name='faculty_marks'),
    # path('faculty/student_data', FacultyStudentDataView, name='faculty_student_data'),
    path('c_admin/', AdminAddAdminView, name='admin_dashboard'),
    path('c_admin/index', AdminAddAdminView, name='admin_add_admin'),
    path('c_admin/add_company', AdminCompanyView, name='admin_add_company'),
    path('c_admin/add_faculty', AdminFacultyView, name='admin_add_faculty'),
    path('c_admin/add_student', AdminStudentView, name='admin_add_student'),
    path('c_admin/login',AdminLoginView,name='admin_login'),
    path('c_admin/logout',AdminLogoutView,name='admin_logout'),
    path('c_admin/forgetPassword',AdminForgetPassView,name='admin_forget'),
    path('logout/',LogoutView,name='logout'),


    path('forgetPassword',ForgetPasswordView,name="forget_password"),

    # path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),
    # url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     activate, name='activate'),
    path('activate/<slug:slug>/<slug:token>',ActivateView,name="activate_link"),
    path('changePassword/<str:slug>',ChangePasswordView,name="change_password")
    # path('c_admin/', c_admin.AdminAddAdminView, name='admin_dashboard'),
    # path('c_admin/index', c_admin.AdminAddAdminView, name='admin_add_admin'),
    # path('c_admin/add_company', c_admin.AdminCompanyView, name='admin_add_company'),
    # path('c_admin/add_faculty', c_admin.AdminFacultyView, name='admin_add_faculty'),
    # path('c_admin/add_student', c_admin.AdminStudentView, name='admin_add_student'),
    # path('c_admin/login',c_admin.AdminLoginView,name='admin_login'),
    # path('c_admin/logout',c_admin.AdminLogoutView,name='admin_logout'),
    # path('forgetPassword',ForgetPasswordView,name="forget_password"),

    # path('logout/',LogoutView,name='logout'),
    # path('changePassword',ChangePasswordView,name="change_password")

#     url(r'students/login',StudentLoginView,name="student_login"),
#     url(r'students/profile', StudentProfileView, name="student_profile"),
#     url(r'students/', StudentDashboardView, name='student_dashboard'),
#     url(r'students/index', StudentDashboardView, name='student_dashboard'),
#    url(r'students/exams', StudentExamView, name='student_exams'),
#     # path('students/assignments', StudentAssignmentView, name='student_assignments'),
#     url(r'students/projects', StudentProjectView, name='student_projects'),
#     # path('students/timetable', StudentTimetableView, name='student_timetable'),
#     url(r'students/achievements', StudentAchievementView, name='student_achievements'),
#     url(r'students/logout', StudentLogoutView, name='student_logout'),
#     url(r'students/forgetPassword', StudentForgetPassView, name='student_forget'),
#     # path('students/materials', StudentMaterialView, name='student_materials'),
#     url(r'faculty/login',FacultyLoginView,name="faculty_login"),
#     url(r'faculty/', FacultyDashboardView, name='faculty_dashboard'),
#     url(r'faculty/index', FacultyDashboardView, name='faculty_dashboard'),
#     url(r'faculty/profile', FacultyProfileView, name='faculty_profile'),
#     url(r'faculty/add_event', FacultyAddEventView, name='faculty_add_event'),
#     url(r'faculty/events', FacultyEventView, name='faculty_events'),
#     url(r'faculty/logout', FacultyLogoutView, name='faculty_logout'),
#     url(r'faculty/forgetPassword', FacultyForgetPassView, name='faculty_forget'),
#     # path('faculty/materials', FacultyMaterialsView, name='faculty_material'),
#     # path('faculty/view_Marks', FacultyMarksView, name='faculty_marks'),
#     # path('faculty/student_data', FacultyStudentDataView, name='faculty_student_data'),
#     url(r'c_admin/', AdminAddAdminView, name='admin_dashboard'),
#     url(r'c_admin/index', AdminAddAdminView, name='admin_add_admin'),
#     url(r'c_admin/add_company', AdminCompanyView, name='admin_add_company'),
#     url(r'c_admin/add_faculty', AdminFacultyView, name='admin_add_faculty'),
#     url(r'c_admin/add_student', AdminStudentView, name='admin_add_student'),
#     url(r'c_admin/login',AdminLoginView,name='admin_login'),
#     url(r'c_admin/logout',AdminLogoutView,name='admin_logout'),
#     url(r'c_admin/forgetPassword',AdminForgetPassView,name='admin_forget'),
#     url(r'logout/',LogoutView,name='logout'),


#     url(r'forgetPassword',ForgetPasswordView,name="forget_password"),

#     # path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),
#     url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
#         activate, name='activate'),
#     url(r'changePassword',ChangePasswordView,name="change_password")
]