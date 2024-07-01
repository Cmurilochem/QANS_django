from django.shortcuts import get_object_or_404, render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Survey, Question, Response, Answer
from .forms import SurveyForm, QuestionForm, ResponseForm, AnswerForm


def home(request):
    return render(request, 'qqe/home.html')


def survey_details(request, survey_id):
    survey = get_object_or_404(Survey, pk=survey_id)
    return render(request, "qqe/survey_details.html", {"survey": survey})


@login_required
def profile(request):
    return render(request, 'qqe/profile.html')


@login_required
def create_survey(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            survey = form.save(commit=False)
            survey.created_by = request.user
            survey.save()
            return redirect('survey_list')
    else:
        form = SurveyForm()
    return render(request, 'qqe/create_survey.html', {'form': form})


@login_required
def survey_list(request):
    surveys = Survey.objects.all()
    return render(request, 'qqe/survey_list.html', {'surveys': surveys})


@login_required
def submit_response(request, survey_id):
    survey = Survey.objects.get(id=survey_id)
    if request.method == 'POST':
        response_form = ResponseForm(request.POST)
        if response_form.is_valid():
            response = response_form.save(commit=False)
            response.survey = survey
            response.save()
            for question in survey.questions.all():
                answer_text = request.POST.get(f'question_{question.id}')
                Answer.objects.create(response=response, question=question, text=answer_text)
            return redirect('thank_you')
    else:
        response_form = ResponseForm()
    return render(request, 'qqe/submit_response.html', {'survey': survey, 'response_form': response_form})


@login_required
def survey_report(request, survey_id):
    survey = Survey.objects.get(id=survey_id)
    responses = Response.objects.filter(survey=survey)
    return render(request, 'qqe/survey_report.html', {'survey': survey, 'responses': responses})

