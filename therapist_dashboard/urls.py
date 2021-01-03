from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
app_name="therapist_dashboard"
urlpatterns = [
	path('profile/',views.ProfileView.as_view(),name='profile'),
	path('patients/',views.PatientsView.as_view()),
	path('questions/',views.QuestionView.as_view()),
	path('questions/<int:pk>/your_answers/',views.AnswerView.as_view()),
	path('questions/<int:pk>/answer/',views.NewAnswerView),
	path('questions/<int:pk>/your_answers/<int:pk_alt>/edit/',views.AnswerUpdateView),
]