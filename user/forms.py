import user
from django import forms
from user.models import User
from django.db.models import Q
from phonenumber_field.formfields import PhoneNumberField

class LoginForm(forms.Form):
    username = forms.CharField(label = "Username")
    password = forms.CharField(label = "Password",widget = forms.PasswordInput)

class RegisterForm(forms.Form):
    
    email = forms.CharField(max_length=50, label="Email")
    username = forms.CharField(max_length = 50,label = "Username")
    password = forms.CharField(max_length=20,label = "Passowrd",widget = forms.PasswordInput)
    confirm = forms.CharField(max_length=20,label ="Confirm Password",widget = forms.PasswordInput)
    phone =  PhoneNumberField()
    
    def clean(self):
        username = self.cleaned_data.get("username")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")
        phone = self.cleaned_data.get('phone')

        if User.objects.filter(Q(username=username)| Q(email=email)).exists():
            raise forms.ValidationError("Username/Email already exists")

        if (password) and (confirm) and (password != confirm):
            raise forms.ValidationError("Passwords do not match")

        values = {
            "username" : username,
            "password" : password,
            "email" : email,
            "phone": phone
        }
        return values


