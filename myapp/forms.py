from django import forms
from myapp.models import *

class User(forms.ModelForm):
          class Meta:
                    model=NewUser
                    fields='__all__'

class CheckUser(forms.ModelForm):
          class Meta:
                    model=CheckNewUser
                    fields='__all__'
                    
                    
