from django.db import models
from django.conf import settings
from authentication.models import School
class VerificationQuestions(models.Model):
    question = models.CharField(max_length=256, blank=True, verbose_name='Question')
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
    on_delete=models.PROTECT,related_name='mission_created_by' ,verbose_name='created by' )
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

class MissionConfiguration(models.Model):
    
    mission = models.ForeignKey(Mission,null=True, blank=True,on_delete=models.PROTECT,related_name='mission_conf' ,verbose_name='Mission ')
    school = models.ForeignKey(School,null=True, blank=True,on_delete=models.PROTECT,related_name='school_agent_conf' ,verbose_name='School')
    agents = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True,verbose_name='Agents' )
    configure_by = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True,
    on_delete=models.PROTECT,related_name='mission_configure_by' ,verbose_name='configure by' )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.mission} :-> {self.school}"
    
    class Meta:
        verbose_name_plural = "Mission conf"
        db_table = "mission_configurations"
        
class Finalist(models.Model):
    mission_configuration = models.ForeignKey(MissionConfiguration,null=True, blank=True,
        on_delete=models.PROTECT,related_name='mission_configurations' ,verbose_name='School' )
    registration_number = models.CharField(max_length=15,default='-',null=True, blank=True, verbose_name='Registration number')
    student_names = models.CharField(max_length=50,default='-',null=True, blank=True, verbose_name='Student names')
    place_of_birth = models.CharField(max_length=50,default='-',null=True, blank=True, verbose_name='place of birth')
    date_of_birth = models.CharField(max_length=50,default='-',null=True, blank=True, verbose_name='date of birth')
    gender = models.CharField(max_length=20, blank=True,  default='Masculin',
		choices=(
			('Masculin', 'Masculin'),
			('Femini', 'Femini')			
		),
        verbose_name='Gender',
    )
    level = models.CharField(max_length=20, blank=True,  default='LICENCE',
		choices=(
			('LICENCE', 'LICENCE'),
			('MAITRISE', 'MAITRISE'),			
			('DOCTORAT', 'DOCTORAT'),			
			('BREVET', 'BREVET'),			
		),
        verbose_name='level',
    )
    faculty = models.CharField(max_length=256,default='-',null=True, blank=True, verbose_name='faculty')
    option = models.CharField(max_length=256,default='-',null=True, blank=True, verbose_name='option')
    status = models.CharField(max_length=20, blank=True,  default='waiting',
		choices=(
			('waiting', 'waiting'),
			('order', 'order'),			
		),
        verbose_name='Status',
    )
    controller_by = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True,
        on_delete=models.PROTECT,related_name='finalist_controller_by' ,verbose_name='controller by' )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.student_names}"
    
    class Meta:
        verbose_name_plural = "Finalist"
        db_table = "finalists"

class Controller(models.Model):
    question = models.ForeignKey(VerificationQuestions, null=True, blank=True,
                on_delete=models.PROTECT,related_name='controller_question',verbose_name='Question' )
    response = models.CharField(max_length=256,default='-',null=True, blank=True, verbose_name='Response')
    finalist = models.ForeignKey(Finalist, null=True, blank=True,
                on_delete=models.PROTECT,related_name='controller_finalist',verbose_name='Finalist' )
    controller_by = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True,
                    on_delete=models.PROTECT,related_name='controller_by' ,verbose_name='controller by' )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.finalist.student_names}"
    
    class Meta:
        verbose_name_plural = "Controllers"
        db_table = "controllers"