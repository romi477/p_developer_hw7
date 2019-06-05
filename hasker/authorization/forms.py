from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Test

from django.forms import ModelForm


class TestForm(ModelForm):
    class Meta:
        model = Test
        fields = ('person', 'avatar')


class UserCreateForm(UserCreationForm):
    # email = forms.EmailField(required=True)
    avatar = forms.ImageField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'avatar', 'password1', 'password2',)

    # def save(self, commit=True):
    #     user = super(UserCreateForm, self).save(commit=False)
    #     # user.email = self.cleaned_data['email']
    #     user.profile.avatar = self.cleaned_data['avatar']
    #     if commit:
    #         user.save()
    #     return user

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     try:
    #         User.objects.get(email__iexact=email)
    #     except User.DoesNotExist:
    #         return email
    #     raise forms.ValidationError("This email address is already in use.")
    #
    



    # email = forms.EmailField(required=True)
    #
    # class Meta:
    #     model = apps.get_model('forum', 'MyUser')
    #     fields = ('username', 'email', 'avatar')
    #
    #     def save(self, commit=True):
    #         user = super(UserCreateForm, self).save(commit=False)
    #         user.email = self.cleaned_data['email']
    #         if commit:
    #             user.save()
    #         return user

