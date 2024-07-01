import uuid
from django.db import models
from django.contrib.auth.models import User


class Survey(models.Model):
    survey_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    survey_title = models.CharField(max_length=200)
    survey_description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.survey_title


class Question(models.Model):
    survey_name = models.ForeignKey(Survey, related_name='questions', on_delete=models.CASCADE)
    question_text = models.CharField(max_length=500)

    def __str__(self):
        return self.question_text


class Response(models.Model):
    survey_name = models.ForeignKey(Survey, on_delete=models.CASCADE)
    respondent_id = models.CharField(max_length=100)  # Anonymize respondent
    submitted_at = models.DateTimeField(auto_now_add=True)


class Answer(models.Model):
    response = models.ForeignKey(Response, related_name='answers', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField()
