from django import forms
from .models import Comment, Event

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['date', 'details']