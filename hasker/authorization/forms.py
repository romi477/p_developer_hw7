from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Person, PersonProfile, Test
from django.forms import ModelForm


class TestForm(ModelForm):
    class Meta:
        model = Test
        fields = ('person', 'avatar')


class PersonForm(UserCreationForm):
    avatar = forms.ImageField(required=False)

    class Meta:
        model = Person
        fields = ('username', 'email', 'avatar', 'password1', 'password2',)

    # def save(self, commit=True):
    #     person = super(PersonForm, self).save(commit=False)
    #     person.profile.avatar = self.cleaned_data['avatar']
    #     if commit:
    #         person.save()
    #     return person


class ProfileForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = PersonProfile
        fields = ('email', 'avatar')
