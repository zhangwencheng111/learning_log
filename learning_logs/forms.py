from django import forms
from learning_logs.models import Topic, Entry


class TopicForm(forms.ModelForm):
	class Meta:
		model = Topic
		fields = ["title"]
		labels = {"title":""}


class EntryForm(forms.ModelForm):
	class Meta:
		model = Entry
		fields = ["text"]
		labels = {"text":""}
		widgets = {"text": forms.Textarea(attrs={'cols':80})}