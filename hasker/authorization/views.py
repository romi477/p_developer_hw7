from .models import Person
from django.apps import apps
from django.views import View
from django.conf import settings
from django.shortcuts import render
from .forms import PersonForm, PersonProfile
from django.contrib.auth import login, logout
from django.http import HttpResponseForbidden
from django.views.generic.edit import FormView
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


class RegistrationFormView(FormView):
    form_class = PersonForm
    success_url = '/hasker/'
    template_name = 'authorization/registration.html'

    def form_valid(self, form):
        self.user = form.save()
        login(self.request, self.user)
        return super(RegistrationFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegistrationFormView, self).form_invalid(form)


class UpdateProfile(View):
    
    def get(self, request):
        person = Person.objects.get(username=request.user.username)
        bound_form = PersonProfile(instance=person)
        return render(request, 'authorization/profile_update.html', {'form': bound_form, 'person': person})

    def post(self, request):
        person = Person.objects.get(username=request.user.username)
        bound_form = PersonProfile(request.POST, request.FILES, instance=person)
        
        if bound_form.is_valid():
            bound_form.save()
            return redirect('person_profile')
        return render(request, 'authorization/profile_update.html', {'form': bound_form, 'person': person})


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
        return redirect('index')


@login_required(login_url=settings.LOGIN_URL)
def person_profile(request):
    person = Person.objects.get(username=request.user.username)
    return render(request, 'authorization/_profile.html', {'person': person})


def person_profile_questions(request):
    if request.user.is_authenticated:
        question = apps.get_model('forum', 'Question')
        questions = question.objects.filter(author__username=request.user.username)
        return render(request, 'authorization/_questions.html', {'questions': questions})
    return HttpResponseForbidden('403, Forbidden')


@login_required(login_url=settings.LOGIN_URL)
def person_free_info(request, nickname):
    if request.user.username == nickname:
        return redirect('person_profile')
    person = get_object_or_404(Person, username=nickname)
    return render(request, 'authorization/_profile.html', {'person': person, 'nickname': nickname})


