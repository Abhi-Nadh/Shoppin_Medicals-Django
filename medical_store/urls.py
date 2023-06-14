
from django.urls import path
from . import views

urlpatterns = [
        path('',views.medlist,name='medicinelist'),
        path('signup',views.signup_user,name='signup'),
        path('login',views.login_user,name='login'),
        path('logout',views.logout_user,name='logout'),
        path('addmedicine',views.addmed,name='addmedicine'),
        path('editmedicine/<int:uid>',views.updatemed,name='editmedicine'),
        path('deletemedicine/<int:uid>',views.delete_medicine,name='deletemedicine'),
                ]