from pagedown.widgets import PagedownWidget
# from markdown_deux.templatetags.markdown_deux_tags import markdown_allowed
from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    entry = forms.CharField(widget=PagedownWidget())

    class Meta:
        model = Entry
        fields = ['entry']
        labels = {'entry': ''}
        
