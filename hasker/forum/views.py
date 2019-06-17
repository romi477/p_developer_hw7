from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from .models import Question, Tag
from .forms import QuestionForm
from django.contrib.auth.decorators import login_required
from django.conf import settings



def tag_questions(request, tag):
    questions = Question.objects.filter(tags__name=tag)
    return render(request, 'forum/tag_questions_list.html', {'questions': questions, 'tagname': tag})


class TagListView(ListView):
    model = Tag
    template_name = 'forum/tag_list.html'
    context_object_name = 'tag_list'
    ordering = ('name',)


class QuestionDetail(DetailView):
    model = Question
    template_name = 'forum/question_detail.html'
    context_object_name = 'question'
    
    # def get_queryset(self, slug):
    #     question = self.model.objects.get(slug=slug)
    
    
    # def get_context_data(self, **kwargs):
    #     context = super(QuestionDetail, self).get_context_data(**kwargs)



class AnswerCreate(FormView):
    pass


class QuestionCreate(FormView):
    form_class = QuestionForm
    success_url = '/hasker/'
    template_name = 'forum/add_question.html'
    
    def form_valid(self, form):
        self.question = form.save(commit=False)
        self.question.author = self.request.user
        tag_list = form.cleaned_data['tags']
        self.question.save(tag_list=tag_list)
        return super(QuestionCreate, self).form_valid(form)
    
    def form_invalid(self, form):
        return super(QuestionCreate, self).form_invalid(form)


class Index(ListView):
    model = Question
    template_name = 'forum/index.html'
    context_object_name = 'questions'
    paginate_by = 20

    def get_queryset(self):
        return self.model.objects.all().order_by('-pub_date')

def test(request):
    return HttpResponse(f'<div>{request.method}</div>\n\n{request.environ}')

def index(request):
    return render(request, 'forum/index.html', {})


