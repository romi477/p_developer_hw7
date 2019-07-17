from django.db.models import Q
from django.shortcuts import render
from django.shortcuts import reverse
from .forms import QuestionForm, ReplyForm
from .models import Question, Tag, Reply, Vote
from django.views.generic.edit import FormView
from django.http import JsonResponse, HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.list import MultipleObjectMixin
from django.contrib.contenttypes.models import ContentType


class Index(ListView):
    model = Question
    template_name = 'forum/index.html'
    context_object_name = 'questions'
    paginate_by = 20

    def get_queryset(self):
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = Question.objects.filter(Q(title__icontains=search_query) | Q(content__icontains=search_query))
            return queryset
        return self.model.objects.order_by('-pub_date')


class TagListView(ListView):
    model = Tag
    template_name = 'forum/tag_list.html'
    context_object_name = 'tag_list'
    paginate_by = 20

    def get_queryset(self):
        queryset = Tag.objects.all()
        t_sorted = sorted(queryset, key=lambda tag: -tag.questions.count())
        return t_sorted


def hot_questions(request):
    """
    отношение GenericRelation(Vote) дублирует записи в кверисете по количеству votes,
    distinct() для  sqlite не отрабатывал, пришлось взять set()
    """
    questions = Question.objects.order_by('votes', '-pub_date')[:10]
    q_sorted = sorted(set(questions), key=lambda question: -question.total_votes)
    return render(request, 'forum/questions_list.html', {'questions': q_sorted})


def tag_questions(request, tag_name):
    questions = Question.objects.filter(tags__name=tag_name)
    return render(request, 'forum/tag_questions.html', {'questions': questions, 'tag': tag_name})


class QuestionDetail(DetailView, MultipleObjectMixin):
    model = Question
    template_name = 'forum/question_detail.html'
    context_object_name = 'question'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        replies = Reply.objects.filter(related_q__slug=self.kwargs['slug']).order_by('pub_date')
        context = super(QuestionDetail, self).get_context_data(object_list=replies, **kwargs)
        if self.request.user.is_authenticated:
            context['reply_form'] = ReplyForm()
        return context


def like(request, slug, reply_pk=None):
    if not request.is_ajax():
        return HttpResponse('It is not an ajax request!')
    
    if reply_pk:
        model_obj = Reply.objects.get(pk=reply_pk)
    else:
        model_obj = Question.objects.get(slug=slug)

    model_obj_type = ContentType.objects.get_for_model(model_obj)

    vote, is_created = Vote.objects.get_or_create(
        content_type=model_obj_type,
        object_id=model_obj.id,
        user=request.user
    )
    model_obj.refresh_from_db()
    
    return JsonResponse({'id': reply_pk, 'rating': model_obj.total_votes})


def dislike(request, slug, reply_pk=None):
    if not request.is_ajax():
        return HttpResponse('It is not an ajax request!')
    
    if reply_pk:
        model_obj = Reply.objects.get(pk=reply_pk)
    else:
        model_obj = Question.objects.get(slug=slug)

    model_obj_type = ContentType.objects.get_for_model(model_obj)

    Vote.objects.filter(
        content_type=model_obj_type,
        object_id=model_obj.id,
        user=request.user
    ).delete()
    model_obj.refresh_from_db()
    return JsonResponse({'id': reply_pk, 'rating': model_obj.total_votes})


def add_medal(request, slug, reply_pk):
    if not request.is_ajax():
        return HttpResponse('It is not an ajax request!')
    
    reply = Reply.objects.get(pk=reply_pk)
    
    if request.user.username == reply.related_q.author.username:
        reply.flag = not reply.flag
        reply.save()
        return JsonResponse({'flag': reply.flag})
    

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


