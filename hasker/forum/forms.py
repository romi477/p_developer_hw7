from django import forms
from .models import Question, Reply
from django.forms import ModelForm


class QuestionForm(ModelForm):
    tags = forms.CharField(required=False)

    def clean_tags(self):
        tags = self.cleaned_data.get('tags')
        if not tags:
            return []
        return [t.strip() for t in tags.split(',')[:3]]

    class Meta:
        model = Question
        fields = ('title', 'content', 'tags')


class ReplyForm(forms.Form):
    body = forms.CharField(label='my reply', widget=forms.Textarea(attrs={'rows': 5}))

    def save(self, author, related_q):
        my_reply = Reply.objects.create(
            body=self.cleaned_data['body'],
            author=author,
            related_q=related_q
        )
        return my_reply
