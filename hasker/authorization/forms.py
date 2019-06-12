from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Person


class PersonForm(UserCreationForm):

    class Meta:
        model = Person
        fields = ('username', 'email', 'avatar', 'password1', 'password2',)


class PersonProfile(UserChangeForm):

    class Meta:
        model = Person
        fields = ('email', 'avatar')

