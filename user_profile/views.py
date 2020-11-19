from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from accounts.models import Profile
from community_forum.models import Questions,Answers,QuestionVotes,AnswerVotes
class ProfileView(View,LoginRequiredMixin):
    def get(self, request, *args, **kwargs):

        user_=self.request.user
        user=get_object_or_404(Profile,user=user_)
        context={
            'user':user
        }
        return render(request,'user_profile/profile.html',context)

class MyQuestionsView(View,LoginRequiredMixin):
	def get(self,request,*args,**kwargs):
		questions=get_object_or_404(Questions,user=self.request.user.profile)
		context={
			'questions':questions
		}
		return render(request,'user_profile/questions.html',context)

class MyAnswersView(View,LoginRequiredMixin):
	def get(self,request,*args,**kwargs):
		answers=get_object_or_404(Answers,user=self.request.user.profile)
		context={
			'answers':answers
		}
		return render(request,'user_profile/answers.html',context)


