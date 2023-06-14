from django import forms
from medical_store.models import MedicineData


class SignupForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control username','placeholder':'Username'}), max_length=50, required=True)
    firstname=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Firstname'}), max_length=50, required=True)
    lastname=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Lastname'}), max_length=50, required=True)
    emailid=forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}), max_length=50, required=True)
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}), max_length=16, required=True)

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control username','placeholder':'Username'}), max_length=50, required=True)
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}), max_length=16, required=True)

class Add_medicine(forms.ModelForm):
    class Meta:
        model = MedicineData
        fields = ['medicine_name','company','price', 'medicine_description']
        widgets = {
            'medicine_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Medicine Name'}),
            'company': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Medicine Name'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Price'}),
            'medicine_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'cols': 15, 'placeholder': 'Medicine Description'}),
            }

class SearchForm(forms.Form):
    search_q = forms.CharField(max_length=100, required=False)