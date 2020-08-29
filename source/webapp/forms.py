from django import forms
from .models import *


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['question']


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text']


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['choice']
        widgets = {'choice': forms.CheckboxInput}
