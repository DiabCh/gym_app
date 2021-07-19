from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import password_validators_help_text_html
from django.contrib.auth.password_validation import validate_password
AuthUserModel = get_user_model()


class RegisterForm(forms.Form):
    first_name = forms.CharField(
        label='First Name',
        max_length=255,
        required=True
    )
    last_name = forms.CharField(
        label='Last Name',
        max_length=255,
        required=True
    )
    email = forms.EmailField(
        label='Email Address',
        required=True
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput,
        required=True,
        help_text=password_validators_help_text_html()
    )
    password_confirmation = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput,
        required=True,
        help_text='Please confirm your password'
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            AuthUserModel.objects.get(email=email)
        except AuthUserModel.DoesNotExist:
            return email
        else:
            raise forms.ValidationError('This email is already in use')

    def clean_password(self):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        user = AuthUserModel(
            first_name=first_name,
            last_name=last_name,
            email=email,
        )
        validate_password(password, user)
        return password

    def clean_password_confirmation(self):
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')
        if password != password_confirmation:
            raise forms.ValidationError('the passwords do not match')
        return password_confirmation

    def save(self, commit=True):
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        user = AuthUserModel.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )
        return user

