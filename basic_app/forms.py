from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserAmount

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')


class UserAmountForm(forms.ModelForm):
    amounts = forms.DecimalField(max_digits=6, decimal_places=2)
    class Meta:
        model = UserAmount
        fields = ('amounts',)