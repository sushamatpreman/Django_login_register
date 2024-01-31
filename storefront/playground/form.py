from django import forms
from .models import category

class AddForm(forms.ModelForm):
    class Meta:
        model=category

        fields=('firstname','lastname','email','phonenumber','password','confirmpassword','gender')


        widgets={
            'firstname':forms.TextInput(attrs={'class':'form-contro'}),
            'lastname':forms.TextInput(attrs={'class':'form-contro'}),
            'email':forms.TextInput(attrs={'class':'form-contro'}),
            'phonenumber':forms.TextInput(attrs={'class':'form-contro'}),
            'password':forms.TextInput(attrs={'class':'form-contro'}),
            'confirmpassword':forms.TextInput(attrs={'class':'form-contro'}),
            'gender':forms.TextInput(attrs={'class':'form-contro'}),
        }