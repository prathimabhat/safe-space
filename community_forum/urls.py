from django.conf.urls import url, include
from django.urls import path
from . import views
app_name="community_forum"
urlpatterns=[
	path('',views.CategoryView.as_view()),
	path('<str:category>/',views.SubforumView),
	path('questions/<int:pk>/',views.QuestionView.as_view()),

]
