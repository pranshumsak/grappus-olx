from django import forms
from api.models.user_models import User, GenderChoices


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'contact_no', 'gender', 'dob', 'image', 'username', 'password']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter last Name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),
            'contact_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Contact Number'}),
            'gender': forms.Select(choices=GenderChoices, attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'}),
            'dob': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file border'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'id': "username", 'placeholder': 'Create Your Unique Username'}),

        }
