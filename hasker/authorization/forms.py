from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.apps import apps




class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = apps.get_model('forum', 'MyUser')
        fields = ('username', 'email', 'avatar')

        def save(self, commit=True):
            user = super(UserCreateForm, self).save(commit=False)
            user.email = self.cleaned_data['email']
            if commit:
                user.save()
            return user

