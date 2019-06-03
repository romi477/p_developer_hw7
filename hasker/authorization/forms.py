from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



class UserCreateForm(UserCreationForm):
    avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'avatar', 'password1', 'password2',)

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     try:
    #         User.objects.get(email__iexact=email)
    #     except User.DoesNotExist:
    #         return email
    #     raise forms.ValidationError("This email address is already in use.")
    #
    # def save(self, commit=True):
    #     user = super(UserCreateForm, self).save(commit=False)
    #     user.avatar = self.cleaned_data['avatar']
    #     if commit:
    #         user.save()
    #     return user



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

