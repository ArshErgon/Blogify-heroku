
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()
class SignInForm(forms.Form):
    username = forms.CharField(
                    widget=forms.TextInput(
                                        attrs={
                                                'class':'form-control',
                                                'placeholder':'User Name'
                                               }
                                      )
                             )

    email = forms.CharField(
                    widget=forms.EmailInput(
                                        attrs={
                                                'class':'form-control',
                                                'placeholder':'example@gmail.com'
                                                }
                                        )
                            )

    password = forms.CharField(
                    widget=forms.PasswordInput(
                                            attrs={
                                                    'class':'form-control'
                                                    }
                                               )
                                    )
    password2 = forms.CharField(
                    label='Conform Password',
                                    widget=forms.PasswordInput(
                                                            attrs={
                                                                    'class':'form-control'
                                                                   }
                                                            )
                                                    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError('Username taken')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not 'gmail.com' in email:
            raise forms.ValidationError("Email must have gmail.com not '%s'"% str(email[-9:]))
        return email

    def clean(self):
        data = self.cleaned_data
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password2 != password1:
            raise forms.ValidationError('Password should match')
        return data
