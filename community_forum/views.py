from django.shortcuts import render,redirect
from community_forum.models import Categories
from django.http import HttpResponse,HttpResponseRedirect
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .forms import AnswerForm,QuestionForm
from community_forum.models import Questions,Answers,Comments
from django.urls import reverse



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
	#question_votes=QuestionVotes.objects.filter(question=category_questions)

	return render(request,'community_forum/subforums.html',
			{'category':category,
			'category_questions':category_questions,
			
			}
		)

class QuestionView(View):

	def get(self,request,*args,**kwargs):
		question_id=kwargs['pk']
		question=Questions.objects.filter(id=question_id)
		answers=Answers.objects.filter(question=question_id)
		#category=Categories.objects.filter(category_name=kwargs['category'])
		context={
			'question':question,
			'answers':answers,
			
		}
		return render(request,'community_forum/questions.html',context)


class AnswerView(CreateView,LoginRequiredMixin):

	model=Answers
	form_class=AnswerForm
	success_url='/community_forum/'
	
	def form_valid(self,form):
		
		
		question_=get_object_or_404(Questions,pk=self.kwargs['pk'])
		category_=get_object_or_404(Categories,category_name=question_.category.category_name)
		obj=form.save(commit=False)
		obj.user=self.request.user.profile
		obj.category=category_
		obj.question=question_
		obj.save()
		return super().form_valid(form)
		#return self.render_to_response(self.get_context_data(form=form))
		

class NewQuestionView(CreateView,LoginRequiredMixin):

	model=Questions
	form_class=QuestionForm
	success_url='/community_forum/'
	
	def form_valid(self,form):
		
		category_=get_object_or_404(Categories,category_name=self.kwargs['category'])
		obj=form.save(commit=False)
		obj.user=self.request.user.profile
		obj.category=category_
		obj.save()
		return super().form_valid(form)
	

def QuestionUpVoteView(request,*args,**kwargs):
	question=get_object_or_404(Questions,id=request.POST.get('question_id_up'))
	question.up_votes.add(request.user.profile)
	return HttpResponseRedirect(reverse('community_forum:question-detail',args=[int(kwargs['pk'])]))

def QuestionDownVoteView(request,*args,**kwargs):
	question=get_object_or_404(Questions,id=request.POST.get('question_id_down'))
	question.down_votes.add(request.user.profile)
	return HttpResponseRedirect(reverse('community_forum:question-detail',args=[int(kwargs['pk'])]))


def AnswerUpVoteView(request,*args,**kwargs):
	answer=get_object_or_404(Answers,id=request.POST.get('answer_id_up'))
	answer.up_votes.add(request.user.profile)
	return HttpResponseRedirect(reverse('community_forum:question-detail',args=[int(kwargs['pk_alt'])]))

def AnswerDownVoteView(request,*args,**kwargs):
	answer=get_object_or_404(Answers,id=request.POST.get('answer_id_down'))
	answer.down_votes.add(request.user.profile)
	return HttpResponseRedirect(reverse('community_forum:question-detail',args=[int(kwargs['pk_alt'])]))

