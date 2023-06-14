from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.urls import reverse

from medical_store.models import MedicineData
from .form import Add_medicine, LoginForm, SearchForm, SignupForm
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

# User Register View Function
def signup_user(request):       
    if request.method=='POST':
        signupform=SignupForm(request.POST)
        if signupform.is_valid():
            user_name=signupform.cleaned_data['username']
            firstname=signupform.cleaned_data['firstname']
            lastname=signupform.cleaned_data['lastname']
            email=signupform.cleaned_data['emailid']
            password=signupform.cleaned_data['password']
            if User.objects.filter(username=user_name).exists():
                signupform=SignupForm(request.POST)
                messages.error(request,"Username already exist,choose another username")
                return redirect('signup')

            else:
                user=User.objects.create_user(username=user_name,
                                              first_name=firstname,
                                              last_name=lastname,
                                              email=email,
                                              password=password)
                user.save()
                return HttpResponseRedirect(reverse('home'))
        else:
            context={'signupform':signupform}
            return render(request,'signup.html',context)
    else:   
        signupform=SignupForm()
    return render(request,'signup.html',{'signupform':signupform})


# User login View Function
def login_user(request):
    if request.method=='POST':
        loginform=LoginForm(request.POST)
        if loginform.is_valid():
            username=loginform.cleaned_data['username']
            password=loginform.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if User.objects.filter(username=username).exists():
                if user is not None:
                    login(request,user)
                    return redirect('medicinelist')
                else:
                    messages.error(request,'incorrect password')
                    return redirect('login')
            else:
                messages.error(request,("Incorrect Username"))
                return redirect('login') 
        else:
            messages.error(request,'Credentials Error')
            return render(request,'login.html',{'loginform':loginform})   
    else:
        loginform=LoginForm()
        return render(request,'login.html',{'loginform':loginform})
           
# listing medicine View Function 
@login_required(login_url='login')
def medlist(request):
    searchform=SearchForm(request.GET)
    medicine_data=MedicineData.objects.all()
    if searchform.is_valid():
        search = searchform.cleaned_data['search_q']
        medicine_data = medicine_data.filter(medicine_name__istartswith=search)

    context = {'medicine_data': medicine_data, 'searchform': searchform}
    return render(request, 'medicinelist.html', context)

    # return render(request,'medicinelist.html',{'listmed':medlist_data})



# adding medicine view funtion
@login_required(login_url='login')
def addmed(request):
    if request.method=='POST':
        addmedicineform=Add_medicine(request.POST)
        if addmedicineform.is_valid():
            addmedicineform.save()
            return HttpResponseRedirect(reverse('medicinelist'))
        else:
            # messages.error(request,"Enter valid data")
            return HttpResponseRedirect(reverse('medicinelist'))
    else:
        addmedicineform=Add_medicine()
        return render(request,'addmedicine.html',{'addmed':addmedicineform})
    
# Update Medical data view Funtion
@login_required(login_url='login')
def updatemed(request,uid):
        data=get_object_or_404(MedicineData,id=uid)
        updatemedicineform=Add_medicine(instance=data)
        if request.method=="POST":
            updatemedicineform=Add_medicine(request.POST,instance=data)
            if updatemedicineform.is_valid():
                updatemedicineform.save()
                return HttpResponseRedirect(reverse('medicinelist'))
        return render(request,'editmedicine.html',{'updateform':updatemedicineform})
    
# logut view funtion
@login_required(login_url='login')
def logout_user(request):
    logout(request)    
    return HttpResponseRedirect(reverse('login'))
# delete view funtion
def delete_medicine(request,uid):
        med_data=get_object_or_404(MedicineData,id=uid)
        med_data.delete()
        return redirect('medicinelist')


    
    
    
    


        
        


