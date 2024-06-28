from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:question_id>/', views.survey_details, name='survey_details')
]