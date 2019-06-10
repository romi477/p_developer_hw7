from django.views import View
from .forms import PersonForm, TestForm, ProfileForm
from django.shortcuts import redirect
from django.views.generic.edit import FormView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render
from django.http import HttpResponse
from .models import Person, PersonProfile
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.views.generic import DetailView
from django.urls import reverse




class UpdateProfile(View):
    
    def get(self, request):
        person = Person.objects.get(username=request.user)
        bound_form = ProfileForm(instance=person)
        return render(request, 'authorization/profile_update_form.html', {'form': bound_form, 'person': person})


    def post(self, request):
        person = Person.objects.get(username=request.user)
        bound_form = ProfileForm(request.POST, instance=person)
        
        if bound_form.is_valid():
            bound_form.save()
            return redirect('person_profile')
        return render(request, 'authorization/profile_update_form.html', {'form': bound_form, 'person': person})




class CreateTest(View):
    
    def get(self, request):
        model_form = TestForm()
        context = {'model_form': model_form, 'object_name': 'Test', 'object_url': 'add_obj'}
        return render(request, 'authorization/add_object.html', context)
 
    def post(self, request):
        bound_form = TestForm(request.POST, request.FILES)
        if bound_form.is_valid():
            bound_form.save()
            return HttpResponse('OK')
        return HttpResponse(bound_form.errors)


class RegistrationFormView(FormView):
    form_class = PersonForm
    success_url = '/hasker/'
    template_name = 'authorization/registration.html'


    def form_valid(self, form):
        self.user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password2'])
        login(self.request, self.user)
        return super(RegistrationFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegistrationFormView, self).form_invalid(form)


def signup(request):
    if request.method == "POST":
        form = PersonForm(request.POST, request.FILES)
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
        form = PersonForm()
    return render(request, 'authorization/registration.html', {'form': form})


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


def person_profile(request):
    try:
        profile = PersonProfile.objects.get(person__username=request.user)
    except ObjectDoesNotExist:
        return redirect('login')
    return render(request, 'authorization/person_profile.html', {'profile': profile})

@login_required(login_url=settings.LOGIN_URL)
def person_info(request, nick):
    try:
        profile_info = PersonProfile.objects.get(person__username=nick)
    except ObjectDoesNotExist:
        return HttpResponse(f'404 User "{nick}" does not exist.')
    return render(request, 'authorization/person_profile.html', {'profile': profile_info, 'nick': nick})

