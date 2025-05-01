from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField()
    contrasenya = forms.CharField(widget=forms.PasswordInput())
