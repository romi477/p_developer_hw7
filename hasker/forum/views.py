from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import FormView
from .models import Tag
from .forms import QuestionForm


class TagListView(ListView):
    model = Tag
    template_name = 'forum/tag_list.html'
    context_object_name = 'tag_list'
    
class QuestionCreate(FormView):
    form_class = QuestionForm
    success_url = '/hasker/'
    template_name = 'forum/add_question.html'
    
    def form_valid(self, form):
        self.user = form.save()
        login(self.request, self.user)
        return super(QuestionCreate, self).form_valid(form)
    
    def form_invalid(self, form):
        return super(QuestionCreate, self).form_invalid(form)




def test(request):
    return HttpResponse(f'<div>{request.method}</div>\n\n{request.environ}')

def index(request):
    return render(request, 'forum/index.html', {})

def AskQuestion():
    pass
