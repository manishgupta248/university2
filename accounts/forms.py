from django import forms
from django.contrib.auth.models import User
from allauth.account.forms import SignupForm
from .models import CustomUser

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'username']

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=255, label='First Name')
    last_name = forms.CharField(max_length=255, label='Last Name')

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user
