
from django.urls import path
from . import views

urlpatterns = [
        path('signupapi',views.signup_user,name='signupapi'),
        path('',views.medlist,name='medicinelistapi'),
        path('loginapi',views.login_user,name='loginapi'),
        path('logoutapi',views.logout_userapi,name='logoutapi'),
        path('addmedicineapi',views.addmed,name='addmedicineapi'),
        path('editmedicineapi/<int:uid>',views.updatemed,name='editmedicineapi'),
        path('deletemedicineapi/<int:uid>',views.delete_medicine,name='deletemedicineapi'),


                ]