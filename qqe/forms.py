from django import forms
from .models import Survey, Question, Response, Answer


class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ['survey_title', 'survey_description']


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']


class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['survey_name', 'respondent_id']


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['response', 'question', 'text']