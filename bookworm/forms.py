from django import forms 
from .models import *

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ['uploaded_date']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = []