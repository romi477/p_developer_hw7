from django.views import View
from .forms import UserCreateForm
from .forms import TestForm
from django.http import JsonResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render
from django.http import HttpResponse



class CreateTest(View):
    
    def get(self, request):
        model_form = TestForm()
        context = {'model_form': model_form, 'object_name': 'Test', 'object_url': 'add_obj'}
        return render(request, 'authorization/add_object.html', context)
 
    def post(self, request):
        bound_form = TestForm(request.POST, request.FILES)
        if bound_form.is_valid():
            obj = bound_form.save()
            return HttpResponse('OK')
        return HttpResponse(bound_form.errors)


class RegistrationFormView(FormView):
    form_class = UserCreateForm
    success_url = '/hasker/'
    template_name = 'authorization/registration.html'


    def form_valid(self, form):
        form.save()
        self.user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password2'])
        login(self.request, self.user)
        return super(RegistrationFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegistrationFormView, self).form_invalid(form)


def signup(request):
    if request.method == "POST":
        form = UserCreateForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.avatar = form.cleaned_data.get("avatar")
            user.save()
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect("index_view")
    
    else:
        form = UserCreateForm()
    return render(request, 'authorization/registration.html', {'form': form})

# def validate_email(request):
#     if request.method == 'GET':
#         email = request.GET.get('email')
#         is_taken = User.objects.filter(email=email).exists()
#         if is_taken:
#             message = 'This email address already exists!!!'
#             data = {'is_taken': message}
#             return JsonResponse(data)
#         else:
#             return JsonResponse({'ok': True})



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