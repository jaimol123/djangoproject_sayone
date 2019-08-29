from django import forms
from .models import *
  
class HotelForm(forms.ModelForm): 
  
    class Meta: 
        model = Hotel 
        fields = ['name2', 'text1','images','status'] 

