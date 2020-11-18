from django.shortcuts import render,reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.views import View
from accounts.models import Therapist
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import QuestionForm
from django.shortcuts import get_object_or_404
from django.views.generic import ListView,DetailView,CreateView
from .models import question_to_therapist,answers_from_therapist
from django.urls import reverse_lazy
class TherapistView(View,LoginRequiredMixin):

	def get(self, request, *args, **kwargs):

		therapists=Therapist.objects.all()
		context={
			'therapists':therapists
		}
		return render(request,'Ask_the_doctor/ask_the_doctor.html',context)



class NewQuestionView(CreateView,LoginRequiredMixin):
	
	model=question_to_therapist
	form_class=QuestionForm
	#success_url='NewQuestionView'
	
	def get_queryset(self):
		self.therapist = get_object_or_404(Therapist, pk=self.kwargs['pk'])
		return Therapist.objects.filter(pk=self.therapist)

	
	def form_valid(self,form):
		therapist_= get_object_or_404(Therapist, pk=self.kwargs['pk'])
		obj=form.save(commit=False)
		obj.user=self.request.user.profile
		obj.therapist=therapist_
		obj.save()
		#return self.render_to_response(self.form_valid(form))
		return self.render_to_response(self.get_context_data(form=form))
		#return super().form_valid(form)


	def get_context_data(self,**kwargs):
		context=super().get_context_data(**kwargs)
		user_=self.request.user.profile
		context["questions"] = question_to_therapist.objects.filter(user=user_).order_by('id')

		return context

	'''def get(self,request,*args,**kwargs):
		return render(request,'ask_the_doctor/ask.html')

	def post(self,request,*args,**kwargs):

		questionform = QuestionForm(request.POST)
		
		therapist_ = get_object_or_404(Therapist, pk=self.kwargs.get('pk'))
		if questionform.is_valid():
			question = questionform.save(commit=False)
			question.user = request.user.profile
			question.therapist=therapist_
			
			question.question=questionform.cleaned_data.get('question')

			question.save()
			return render(request,'ask_the_doctor/ask.html',{'form' :questionform})
			#return render('ask_the_doctor/ask/<int:pk>/')

		return render(request,'ask_the_doctor/')
	'''

class MyQuestions(View,LoginRequiredMixin):

	def get(self,request,*args,**kwargs):
		question_id=kwargs['pk']
		question=question_to_therapist.objects.filter(id=question_id)
		answers=answers_from_therapist.objects.filter(question=question_id)
		context={
			'question':question,
			'answers':answers
		}
		return render(request,'Ask_the_doctor/my_questions.html',context)



