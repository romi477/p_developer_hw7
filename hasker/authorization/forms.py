from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Person, PersonalProfile, Test
from django.forms import ModelForm


class TestForm(ModelForm):
    class Meta:
        model = Test
        fields = ('person', 'avatar')


class PersonCreateForm(UserCreationForm):
    # email = forms.EmailField(required=True)
    avatar = forms.ImageField(required=True)

    class Meta:
        model = Person
        fields = ('username', 'email', 'avatar', 'password1', 'password2',)

    # def save(self, commit=True):
    #     user = super(UserCreateForm, self).save(commit=False)
    #     # user.email = self.cleaned_data['email']
    #     user.profile.avatar = self.cleaned_data['avatar']
    #     if commit:
    #         user.save()
    #     return user

   
class UserProfileForm(forms.ModelForm):
    
    class Meta:
        model = PersonalProfile
        fields = '__all__'
        # fields = ('username', 'email', 'avatar')
        