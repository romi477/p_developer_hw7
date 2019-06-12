from django.views import View
from .forms import PersonForm, PersonProfile
from django.shortcuts import redirect
from django.views.generic.edit import FormView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.conf import settings





class RegistrationFormView(FormView):
    form_class = PersonForm
    success_url = '/hasker/'
    template_name = 'authorization/registration.html'

    def form_valid(self, form):
        # self.user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password2'])
        self.user = form.save()
        login(self.request, self.user)
        return super(RegistrationFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegistrationFormView, self).form_invalid(form)


class UpdateProfile(View):
    
    def get(self, request):
        person = Person.objects.get(username=request.user.username)
        bound_form = PersonProfile(instance=person)
        return render(request, 'authorization/profile_update_form.html', {'form': bound_form, 'person': person})

    def post(self, request):
        person = Person.objects.get(username=request.user.username)
        bound_form = PersonProfile(request.POST, request.FILES, instance=person)
        
        if bound_form.is_valid():
            
            bound_form.save()
            return redirect('person_profile')
        return render(request, 'authorization/profile_update_form.html', {'form': bound_form, 'person': person})


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
        person = Person.objects.get(username=request.user.username)
    except ObjectDoesNotExist:
        return redirect('login')
    return render(request, 'authorization/person_profile.html', {'person': person})


@login_required(login_url=settings.LOGIN_URL)
def person_info(request, nick):
    try:
        person = Person.objects.get(username=nick)
    except ObjectDoesNotExist:
        return HttpResponse(f'404 User "{nick}" does not exist.')
    return render(request, 'authorization/person_profile.html', {'person': person, 'nick': nick})



