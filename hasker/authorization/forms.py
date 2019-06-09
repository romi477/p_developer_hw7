from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Person, PersonProfile, Test
from django.forms import ModelForm


class TestForm(ModelForm):
    class Meta:
        model = Test
        fields = ('person', 'avatar')


class PersonForm(UserCreationForm):
    # email = forms.EmailField(required=True)
    avatar = forms.ImageField(required=False)

    class Meta:
        model = Person
        fields = ('username', 'email', 'avatar', 'password1', 'password2',)

    def save(self, commit=True):
        user = super(PersonForm, self).save(commit=False)
        # user.email = self.cleaned_data['email']
        user.personalprofile.avatar = self.cleaned_data['avatar']
        if commit:
            user.save()
        return user


class ProfileForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = PersonProfile
        fields = ('email', 'avatar')
