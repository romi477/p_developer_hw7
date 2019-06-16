from django import forms
from .models import Question
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

