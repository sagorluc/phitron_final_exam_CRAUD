from django import forms
from crud_app.models import CrudModel

class CrudFrom(forms.ModelForm):
    # name = forms.CharField(widget=forms.TextInput(attrs= {'id': 'required',
    #                                 'placeholder': 'Enter your name'}))
    # phone = forms.CharField(widget=forms.TextInput(attrs= {'id': 'required',
    #                                 'placeholder': 'Enter your phone number'}))
    # email = forms.CharField(widget=forms.CharField(attrs= {'id': 'required',
    #                                 'placeholder': 'Enter your email'}))
    # course = forms.CharField(widget=forms.TextInput(attrs= {'id': 'required',
    #                                 'placeholder': 'Enter your course name'}))
    
    class Meta:
        model = CrudModel
        fields = ['name',
                  'phone', 'email', 'course', 
                  'description']
        
class Update(forms.ModelForm):
    class Meta:
        model = CrudModel
        fields = ['image', 'name', 'phone', 'email', 'course', 'description']
        
        