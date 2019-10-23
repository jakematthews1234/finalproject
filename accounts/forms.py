from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

"""the form for users to login"""
class UserLoginForm(forms.Form):
    username_or_email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

""" the form for users to register an account"""
class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password Confirmation',
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    """ ensures that the data sent to the database is converted into the appropriate data type based on the model """
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'Email addresses must be unique.')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        """ensures password fields are not empty"""
        if not password1 or not password2:
            raise ValidationError("Password must not be empty")

        """ checks to see if both password1 and password2 match for security"""
        if password1 != password2:
            raise ValidationError("Passwords do not match")

        return password2