from django.contrib import admin
from accounts.models import Profile,Therapist,CustomUser
from Ask_the_doctor.models import question_to_therapist,answers_from_therapist
#Register your models here.
admin.site.register(CustomUser)
admin.site.register(Profile)
admin.site.register(Therapist)
admin.site.register(question_to_therapist)
admin.site.register(answers_from_therapist)