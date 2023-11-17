from django.db import models
#from django.contrib.auth.models import User


class EventDetails(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True)
    # Define EventDetails model fields

class JobRequisition(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True)
    # Define JobRequisition model fields

class Persona(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True)
    # Define Persona model fields

class ScreeningMode(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True)
    # Define ScreeningMode model fields

class Gender(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True)
    # Define Gender model fields

class MaritalStatus(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True)
    # Define MaritalStatus model fields

class City(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True)
    # Define City model fields

class ExperienceLevel(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True)
    # Define ExperienceLevel model fields

class EducationLevel(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True)
    # Define EducationLevel model fields

class EducationQualification(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True)
    # Define EducationQualification model fields

class EducationSpecialization(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True)
    # Define EducationSpecialization model fields

class Source(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True)
    # Define Source model fields

class SourceType(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True)
    # Define SourceType model fields

class ReasonForChange(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True)
    # Define ReasonForChange model fields
class EmployeeDirectory(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True)
    # Define EmployeeDirectory model fields

class EducationInstitution(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True)
    # Define EducationInstitution model fields

class Candidate(models.Model):  
    event = models.ForeignKey(EventDetails, models.DO_NOTHING, db_column="event", blank=True, null=True)
    job_position = models.ForeignKey(JobRequisition, models.DO_NOTHING, db_column="job_position", blank=True, null=True)
    recruiter_alert = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    persona = models.ForeignKey(Persona, models.DO_NOTHING, db_column="persona", blank=True, null=True, default=1)
    role = models.IntegerField(blank=True, null=True)
    screening_mode = models.ForeignKey(ScreeningMode, models.DO_NOTHING, db_column="screening_mode", blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    gender = models.ForeignKey(Gender, models.DO_NOTHING, db_column="gender", blank=True, null=True)
    marital_status = models.ForeignKey(MaritalStatus, models.DO_NOTHING, db_column="marital_status", blank=True, null=True)
    contact_no_primary = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    contact_no_alternate = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    referred_by = models.ForeignKey(EmployeeDirectory, models.DO_NOTHING, db_column="referred_by", blank=True, null=True)
    referred_by_other = models.CharField(max_length=250, blank=True, null=True)
    address_line = models.CharField(max_length=255, blank=True, null=True)
    city = models.ForeignKey(City, models.DO_NOTHING, db_column="city", blank=True, null=True)
    pincode = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    experience_level = models.ForeignKey(ExperienceLevel, models.DO_NOTHING, db_column="experience_level", blank=True, null=True)
    education_level = models.ForeignKey(EducationLevel, models.DO_NOTHING, db_column="education_level", blank=True, null=True)
    education_qualification = models.ForeignKey(EducationQualification, models.DO_NOTHING, db_column="education_qualification", blank=True, null=True)
    education_specialization = models.ForeignKey(EducationSpecialization, models.DO_NOTHING, db_column="education_specialization", blank=True, null=True)
    education_specialization_other = models.TextField(blank=True, null=True)
    education_institution = models.ForeignKey(EducationInstitution, models.DO_NOTHING, db_column="education_institution", blank=True, null=True)
    education_institution_other = models.TextField(blank=True, null=True)
    source = models.ForeignKey(Source, models.DO_NOTHING, db_column="source", blank=True, null=True, related_name="source_for_candidate_details")
    source_type = models.ForeignKey(SourceType, models.DO_NOTHING, db_column="source_type", blank=True, null=True)
    years_of_experience = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    current_employer = models.CharField(max_length=100, blank=True, null=True)
    current_designation = models.TextField(blank=True, null=True)
    current_monthly_salary = models.IntegerField(blank=True, null=True)
    expected_monthly_salary = models.IntegerField(blank=True, null=True)
    notice_period = models.CharField(max_length=50, blank=True, null=True)
    reason_for_change = models.ForeignKey(ReasonForChange, models.DO_NOTHING, db_column="reason_for_change", blank=True, null=True)
    photo_path = models.TextField(blank=True, null=True)
    resume_path = models.TextField(blank=True, null=True)
    login_time = models.DateTimeField(blank=True, null=True)
    logout_time = models.DateTimeField(blank=True, null=True)
    ip_address = models.CharField(max_length=15, blank=True, null=True)
    geo_location = models.CharField(max_length=50, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(default=1)

    class Meta:
        #managed = True
        db_table = "Candidate"
        #constraints = [
        #    models.UniqueConstraint(fields=['first_name', 'last_name'], name='full_name')
        #]

#class Candidate(models.Model):
 #   candidatedirectory=models.ForeignKey(CandidateDirectory,models.DO_NOTHING, db_column='candidatedirectory',blank=True,null=True)