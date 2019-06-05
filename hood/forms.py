from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import Profile,Area,Business,Updates

class ProfileForm(forms.ModelForm):

  class Meta:
      model = Profile
      fields = ['profile_photo','neighbourhood']


class HoodForm(forms.ModelForm):
   '''
   To add new neighbourhood data.
   '''
 
   class Meta:
      model = Area
      fields = ['name']

class UpdateForm(forms.ModelForm):

   class Meta:
      model= Updates
      fields = ['title','post','email','posted_by','area']
   
class BusinessForm(forms.ModelForm):

   class Meta:
      model = Business
      fields = ['business_name','email','category']
   


