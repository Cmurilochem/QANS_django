from django.shortcuts import get_object_or_404, render

from . models import Survey


def home(request):
    return render(request, 'qqe/home.html')


def survey_details(request, survey_id):
    survey = get_object_or_404(Survey, pk=survey_id)
    return render(request, "qqe/survey_details.html", {"survey": survey})
