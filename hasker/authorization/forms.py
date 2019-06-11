from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import Person, Test
from django.forms import ModelForm



class PersonForm(UserCreationForm):

    class Meta:
        model = Person
        fields = ('username', 'email', 'avatar', 'password1', 'password2',)


class PersonProfile(UserChangeForm):

    class Meta:
        model = Person
        fields = ('email', 'avatar')


class TestForm(ModelForm):
    class Meta:
        model = Test
        fields = '__all__'
