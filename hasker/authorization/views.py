from django.views import View
from .forms import UserCreateForm
from django.http import JsonResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.contrib.auth import login, logout, authenticate


class RegistrationFormView(FormView):
    form_class = UserCreateForm
    success_url = '/hasker/'
    # success_url = "{% url 'index_view' %}"
    template_name = 'authorization/registration.html'

    def form_valid(self, form):
        form.save()
        self.user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password2'])
        login(self.request, self.user)
        return super(RegistrationFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegistrationFormView, self).form_invalid(form)


def validate_email(request):
    if request.method == 'GET':
        email = request.GET.get('email')
        is_taken = User.objects.filter(email=email).exists()
        if is_taken:
            message = 'This email address already exists!!!'
            data = {'is_taken': message}
            return JsonResponse(data)
        else:
            return JsonResponse({'ok': True})



class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = 'authorization/login.html'
    success_url = '/hasker/'

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(LoginFormView, self).form_invalid(form)



class LogOutFormView(View):
    def get(self, request):
        logout(request)
        return redirect('index_view')


class EditUserForm(UserChangeForm):
    
    pass