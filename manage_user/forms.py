from django import forms
from django.contrib.auth.models import User
from login.models import UserProfile, DataBase
from django.core.exceptions import ValidationError

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')
    databases = forms.ModelMultipleChoiceField(queryset=DataBase.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password','confirm_password','email', 'databases']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('confirm_password')

        if password and password2 and password != password2:
            raise ValidationError("Passwords don't match")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
            custom_user = UserProfile(user=user)
            custom_user.save()
            custom_user.databases.set(self.cleaned_data['databases'])
        return user
