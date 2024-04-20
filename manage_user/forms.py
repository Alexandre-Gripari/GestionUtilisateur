from django import forms
from django.contrib.auth.models import User
from login.models import UserProfile

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    CHOICES = UserProfile.CHOICES

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email']

    choice = forms.ChoiceField(choices=CHOICES)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
    

