from django.db import models

from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils.safestring import mark_safe


class User(AbstractUser):
    school_group = models.ManyToManyField('SchoolGroup', blank=True,verbose_name='school group' )
    role = models.ManyToManyField('Role', blank=True,verbose_name='Roles' )
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    class Meta:
        verbose_name_plural = "Users"
        db_table = "users"

class Role(models.Model):
    name= models.CharField(max_length=350, blank=True, verbose_name='Name')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
        
    def __str__(self):
        return f"{self.name}"
    
class SchoolType(models.Model):

    name= models.CharField(max_length=350, blank=True, verbose_name='Name')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True,
    on_delete=models.PROTECT,related_name='school_type_created_by' ,verbose_name='created_by' )
    attachment= models.ImageField(upload_to='attachment/',verbose_name='attachment',blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name_plural = "School type"
        db_table = "shool_type"

class SchoolGroup(models.Model):
    name = models.CharField(max_length=30, blank=True, verbose_name='Name')
    litera = models.CharField(max_length=5, blank=True,  default='A',
		choices=(
			('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L'), ('M', 'M'), ('N', 'N'), ('O', 'O'), ('P', 'P'), ('Q', 'Q'), ('R', 'R'), ('S', 'S'), ('T', 'T'), ('U', 'U'), ('V', 'V'), ('W', 'W'), ('X', 'X'), ('Y', 'Y'), ('Z', 'Z')			
		),
        verbose_name='Litera',
    )
    school_type = models.ForeignKey(SchoolType, blank=True,
    on_delete=models.PROTECT,related_name='shool_type' ,verbose_name='School type' )
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True,
    on_delete=models.PROTECT,related_name='school_group_created_by' ,verbose_name='created by' )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.school_type.name} :-> {self.name}"
class School (models.Model):

    code = models.CharField(max_length=350, blank=True, verbose_name='Code')
    name = models.CharField(max_length=350, blank=False, verbose_name='name')
    acronym = models.CharField(max_length=350, blank=True, verbose_name='acronym')
    address = models.CharField(max_length=350, blank=False, verbose_name='Address')
    logo = models.ImageField(upload_to='logos/',verbose_name='logo',blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True,
    on_delete=models.PROTECT,related_name='school_created_by' ,verbose_name='created by' )
    school_group = models.ForeignKey(SchoolGroup, blank=True,
    on_delete=models.PROTECT,related_name='shool_group' ,verbose_name='School Group' )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.acronym}"
    
    def _logo(self):
        if self.logo:
            return mark_safe(f'<img src="{self.logo.url}" width="100"/>')
        else:
            return '(no picture)'
    _logo.short_description = 'logo image'
    _logo.allow_tags = True

    class Meta:
        verbose_name_plural = "Schools"
        db_table = "schools"
    




