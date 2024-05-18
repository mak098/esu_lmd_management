from django.contrib import admin
from .models import VerificationQuestions,Mission, MissionConfiguration


@admin.register(VerificationQuestions)
class VerificationQuestionAdmin(admin.ModelAdmin):
    list_display = ['id','question','type']
    fields = ('question','type')
    list_filter =['type',]
    def save_model(self, request, obj, form, change):
            obj.created_by = request.user
            obj.save()

@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    list_display = ['id','academic_year','start_date','start_date','status']
    fields = ['academic_year','start_date','end_date','status']
    list_filter =['status',]
    search_fields =['academic_year',]
    def save_model(self, request, obj, form, change):
            obj.created_by = request.user
            obj.save()
@admin.register(MissionConfiguration)
class MissionConfAdmin(admin.ModelAdmin):
    list_display = ['id','mission','school']
    fields = ['mission','school','agents']
    list_filter =['school','mission',]
    autocomplete_fields = ['school','mission']
    filter_horizontal = ['agents',]
    def save_model(self, request, obj, form, change):
            obj.configure_by = request.user
            obj.save()
    
