from django import forms
from django.contrib.auth.models import User

from .models import Userprofile


class UpdateUserprofileForm(forms.ModelForm):
    avatar = forms.ImageField(required=False, widget=forms.FileInput())
    bio = forms.CharField(required=False, widget=forms.Textarea())

    class Meta:
        model = Userprofile
        fields = ['avatar', 'bio']


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput())
    email = forms.EmailField(required=True, widget=forms.TextInput())

    class Meta:
        model = User
        fields = ['username', 'email']
