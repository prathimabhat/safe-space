from django.conf.urls import url, include
from django.urls import path
from . import views
app_name="community_forum"
urlpatterns=[
	path('',views.CategoryView.as_view()),
	path('<str:category>/',views.SubforumView),
	path('<str:category>/questions/new/',views.NewQuestionView.as_view()),
	path('<str:category>/questions/<int:pk>/',views.QuestionView.as_view()),
	path('<str:category>/questions/<int:pk>/answer/',views.AnswerView.as_view()),

]
