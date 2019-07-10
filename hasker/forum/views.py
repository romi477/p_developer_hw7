from django.shortcuts import render
from django.shortcuts import reverse
from django.db.models import Q
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from .models import Question, Tag, Reply, Vote
from .forms import QuestionForm, ReplyForm
from django.shortcuts import redirect
from django.views.generic.list import MultipleObjectMixin
from django.conf import settings
from django.contrib.contenttypes.models import ContentType


class Index(ListView):
    model = Question
    template_name = 'forum/index.html'
    context_object_name = 'questions'
    paginate_by = 3

    def get_queryset(self):
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = Question.objects.filter(Q(title__icontains=search_query) | Q(content__icontains=search_query))
            return queryset
        return self.model.objects.all().order_by('-pub_date')


class TagListView(ListView):
    model = Tag
    template_name = 'forum/tag_list.html'
    context_object_name = 'tag_list'
    ordering = ('name',)


def tag_questions(request, tag_name):
    questions = Question.objects.filter(tags__name=tag_name)
    return render(request, 'forum/tag_questions.html', {'questions': questions, 'tag': tag_name})


class QuestionDetail(DetailView, MultipleObjectMixin):
    model = Question
    template_name = 'forum/question_detail.html'
    context_object_name = 'question'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        replyes = Reply.objects.filter(related_q__slug=self.kwargs['slug']).order_by('pub_date')
        ctx = super(QuestionDetail, self).get_context_data(object_list=replyes, **kwargs)
        ctx['form'] = ReplyForm()
        return ctx


def like(request, slug, reply_pk):
    reply = Reply.objects.get(pk=reply_pk)

    reply_type = ContentType.objects.get_for_model(reply)

    vote, is_created = Vote.objects.get_or_create(
        content_type=reply_type,
        object_id=reply.id,
        user=request.user
    )
    return redirect('question_detail', slug=slug)


def dislike(request, slug, reply_pk):
    reply = Reply.objects.get(pk=reply_pk)

    reply_type = ContentType.objects.get_for_model(reply)

    Vote.objects.filter(
        content_type=reply_type,
        object_id=reply.id,
        user=request.user
    ).delete()
    return redirect('question_detail', slug=slug)


def add_medal(request, slug, reply_pk):
    reply = Reply.objects.get(pk=reply_pk)
    if reply.flag:
        reply.flag = False
    else:
        reply.flag = True
    reply.save()
    return redirect('question_detail', slug=slug)


class ReplyCreate(FormView):
    form_class = ReplyForm
    template_name = 'forum/question_detail.html'

    def get_success_url(self):
        return reverse('question_detail', kwargs={'slug': self.kwargs['slug']})

    def form_valid(self, form):
        self.author = self.request.user
        self.related_q = Question.objects.get(slug=self.kwargs['slug'])
        self.reply = form.save(author=self.author, related_q=self.related_q)

        link = self.request.build_absolute_uri(reverse('question_detail', kwargs={'slug': self.kwargs['slug']}))
        self.reply.send_email(f'Hi, there is new reply: {link}')
        return super(ReplyCreate, self).form_valid(form)

    def form_invalid(self, form):
        return super(ReplyCreate, self).form_invalid(form)


class QuestionCreate(FormView):
    form_class = QuestionForm
    template_name = 'forum/add_question.html'

    def get_success_url(self):
        return reverse('index')
    
    def form_valid(self, form):
        self.question = form.save(commit=False)
        self.question.author = self.request.user
        tag_list = form.cleaned_data['tags']
        self.question.save(tag_list=tag_list)
        return super(QuestionCreate, self).form_valid(form)
    
    def form_invalid(self, form):
        return super(QuestionCreate, self).form_invalid(form)


