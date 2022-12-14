from unicodedata import name
from django.urls import path
from . import views
from admin_app import views as admin_view

urlpatterns = [
    path('',views.home, name='home'),
    path('general login',views.general_login, name='general_login'),

    path('admission',views.admission, name='admission'),
    path('about',views.about, name='about'),
    path('faq',views.faq, name='faq'),
    path('questionBank',views.questionBank, name='questionBank'),
    path('roadMap',views.roadMap, name='roadMap'),

    path('signinStudent',views.signinStudent, name='signinStudent'),
    path('signinFaculty',views.signinFaculty, name='signinFaculty'),
    path('signinStaffLib',views.signinStaffLib, name='signinStaffLib'),
    path('signinStaffMed',views.signinStaffMed, name='signinStaffMed'),
    path('signup',views.signup, name='signup'),
    path('signout',views.signout, name='signout'),
    path('studentPage',views.studentPage, name='studentPage'),
    path('facultyPage',views.facultyPage, name='facultyPage'),
    path('staffMedPage',views.staffMedPage, name='staffMedPage'),
    path('logout',views.logout_request, name='logout'),
    path('staffLibPage',views.staffLibPage, name='staffLibPage'),
    path('logError',views.logError, name='logError'),
    path('adminHome',admin_view.adminHome,name='adminHome'),
    path('adminStudent',admin_view.adminStudent,name='adminStudent'),
    path('studentregister',admin_view.studentregister,name='studentregister'),

    ]