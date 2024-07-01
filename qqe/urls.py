from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/', include('allauth.urls')),
    path('create_survey/', views.create_survey, name='create_survey'),
    path('survey_list/', views.survey_list, name='survey_list'),
    path('submit_response/<int:survey_id>/', views.submit_response, name='submit_response'),
    path('survey_report/<int:survey_id>/', views.survey_report, name='survey_report'),
    path('profile/', views.profile, name='profile'),  # Add this line
    path('', views.survey_details, name='survey_details')
]