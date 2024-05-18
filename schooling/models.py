from django.db import models
from django.conf import settings
from authentication.models import School
class VerificationQuestions(models.Model):
    question = models.CharField(max_length=30, blank=True, verbose_name='Question')
    type = models.CharField(max_length=20, blank=True,  default='boolean',
		choices=(
			('boolean', 'boolean'),
			('text', 'text'),
			('file', 'file')			
		),
        verbose_name='Type',
    )
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True,
    on_delete=models.PROTECT,related_name='question_created_by' ,verbose_name='created by' )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.question}"
    
    class Meta:
        verbose_name_plural = "Verification questions"
        db_table = "verification_questions"

class  Mission(models.Model):
    academic_year = models.CharField(max_length=30, blank=True, verbose_name='Academic year')
    start_date = models.DateTimeField(verbose_name='Start date')
    end_date = models.DateTimeField(verbose_name='End date')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True,
    on_delete=models.PROTECT,related_name='question_created_by' ,verbose_name='created by' )
    status = models.CharField(max_length=20, blank=True,  default='waiting',
		choices=(
			('waiting', 'waiting'),
			('open', 'open'),
			('close', 'close')			
		),
        verbose_name='Status',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.academic_year}"
    
    class Meta:
        verbose_name_plural = "Missions"
        db_table = "missions"

class DistributionOfAgentsToSchools(models.Model):
    school = models.ForeignKey(School,null=True, blank=True,on_delete=models.PROTECT,related_name='school_agent_order' ,verbose_name='school order' )