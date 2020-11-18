from django.shortcuts import render
from community_forum.models import Categories
from django.http import HttpResponse,HttpResponseRedirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from .forms import AnswerForm
from community_forum.models import Questions,Answers,Comments,QuestionVotes,AnswerVotes
# Create your views here.
class CategoryView(View):

	def get(self, request, *args, **kwargs):

		categories=Categories.objects.order_by('category_name')
		context={
			'categories':categories
		}
		return render(request,'community_forum/categories.html',context)

def SubforumView(request,*args,**kwargs):
	category=kwargs['category']
	category_=get_object_or_404(Categories,category_name=category)
	category_questions=Questions.objects.filter(category=category_)
	question_votes=QuestionVotes.objects.filter(question=category_questions)

	return render(request,'community_forum/subforums.html',
			{'category':category,
			'category_questions':category_questions,
			'question_votes':question_votes
			}
		)

class QuestionView(View):

	def get(self,request,*args,**kwargs):
		question_id=kwargs['pk']
		question=Questions.objects.filter(id=question_id)
		answers=Answers.objects.filter(question=question_id)
		context={
			'question':question,
			'answers':answers
		}
		return render(request,'community_forum/questions.html',context)

class AnswerView(View,LoginRequiredMixin):
	def post(self,request,*args,**kwargs):
		answerform=AnswerForm(request.POST)
		if answerform.is_valid():
			answer = answerform.save(commit=False)
			answer.user = request.user.profile
			answer.question=Questions.objects.filter(id=kwargs['pk'])
			answer=answerform.cleaned_data.get('answer')
