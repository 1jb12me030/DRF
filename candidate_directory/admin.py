from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Candidate)
admin.site.register(EventDetails)
admin.site.register(JobRequisition)
admin.site.register(Persona)
admin.site.register(ScreeningMode)
admin.site.register(Gender)
admin.site.register(MaritalStatus)
admin.site.register(City)
admin.site.register(ExperienceLevel)
admin.site.register(EducationLevel)
admin.site.register(EducationQualification)
admin.site.register(EducationSpecialization)
admin.site.register(Source)
admin.site.register(SourceType)
admin.site.register(ReasonForChange)
