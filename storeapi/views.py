from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.status import ( HTTP_200_OK,HTTP_400_BAD_REQUEST,HTTP_404_NOT_FOUND)
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.contrib.auth.models import User
from medical_store.form import Add_medicine, LoginForm, SearchForm, SignupForm
from django.contrib.auth import login,logout,authenticate
from rest_framework.authtoken.models import Token

from medical_store.models import MedicineData
from storeapi.serializers import MedicineSerializer



@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def signup_user(request):       
    signupform=SignupForm(request.data)
    if signupform.is_valid():
        user_name=signupform.cleaned_data['username']
        firstname=signupform.cleaned_data['firstname']
        lastname=signupform.cleaned_data['lastname']
        email=signupform.cleaned_data['emailid']
        password=signupform.cleaned_data['password']
        if User.objects.filter(username=user_name).exists():
            context={'signupform':signupform.data,'error':'Username already exists'}
            return Response(context,status=HTTP_400_BAD_REQUEST)
        else:
            user=User.objects.create_user(username=user_name,
                                          first_name=firstname,
                                          last_name=lastname,
                                          email=email,
                                          password=password)
            user.save()
            context={'signupform':signupform.data,'success':'Created User'}
        return Response(context,status=HTTP_200_OK)
    else:
        context={'signupform':signupform.data,'error':signupform.errors}
        return Response(context,status=HTTP_400_BAD_REQUEST)  
@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,)) 
def login_user(request):
    login_form = LoginForm(request.data)
    
    if login_form.is_valid():
        username = login_form.cleaned_data['username']
        password = login_form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        if user is None:
            return Response({"error": "Please provide login credentials"}, status=HTTP_400_BAD_REQUEST)
        if not user:
            return Response({"error": "Invalid Credentials"}, status=HTTP_404_NOT_FOUND)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=HTTP_200_OK)
    return Response({"error": "Invalid form data"}, status=HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET'])
@permission_classes((IsAuthenticated,)) 
def medlist(request):
    search=request.query_params.get('search','')
    if search:
        medicine_data = MedicineData.objects.filter(medicine_name__istartswith=search)
        if not medicine_data:
            return Response({'message': 'No matches found'},status=HTTP_404_NOT_FOUND)
    else:    
            medicine_data=MedicineData.objects.all()
    serializer=MedicineSerializer(medicine_data,many=True)
    return Response(serializer.data)

@csrf_exempt
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def addmed(request):
    addmedicineform=Add_medicine(request.POST)
    if addmedicineform.is_valid():
        addmedicineform.save()
        context={'med_form':addmedicineform.data,'success':'Medicine Added'}
        return Response(context,status=HTTP_200_OK)
    else:
        context={'med_form':addmedicineform.data,'error':addmedicineform.errors}
        return Response(context,status=HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def updatemed(request,uid):
        med = MedicineData.objects.get(id=uid)
        serializer=MedicineSerializer(instance=med,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        else:
            return Response(serializer.errors,status=HTTP_404_NOT_FOUND)
        
@csrf_exempt
@api_view(['DELETE'])
@permission_classes((IsAuthenticated,))
def delete_medicine(request,uid):
    med_data=get_object_or_404(MedicineData,id=uid)
    med_data.delete()
    return Response({"Success":"Medicine Deleted"})

@csrf_exempt
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def logout_userapi(request):
    logout(request)    
    
    return Response({"Success": "User logged out"},status=HTTP_200_OK)




