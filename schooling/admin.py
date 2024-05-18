from django.contrib import admin
from .models import VerificationQuestions,Mission, MissionConfiguration,Finalist,Controller


@admin.register(VerificationQuestions)
class VerificationQuestionAdmin(admin.ModelAdmin):
    list_display = ['id','question','type']
    fields = ('question','type')
    list_filter =['type',]
    search_fields = ("question",)
    def save_model(self, request, obj, form, change):
            obj.created_by = request.user
            obj.save()

@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    list_display = ['academic_year','start_date','start_date','status']
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
    search_fields = ['mission','school']
    autocomplete_fields = ['school','mission']
    filter_horizontal = ['agents',]
    def save_model(self, request, obj, form, change):
            obj.configure_by = request.user
            obj.save()
@admin.register(Finalist)
class FinalistAdmin(admin.ModelAdmin):
    list_display = ['registration_number','student_names']
    search_fields = ['registration_number','student_names']
    autocomplete_fields = ['mission_configuration',]
    list_filter =['mission_configuration__mission','mission_configuration__school','controller_by']
    fieldsets = (
        (None, {
            'fields': ('mission_configuration',),
        }),
        ('student info', {
            'fields': ('registration_number','student_names','place_of_birth','date_of_birth','gender',),
        }),
        ('school info', {
            'fields': ('level','faculty','option',),
        }),
        ('status', {
            'fields': ('status',),
        }),
        )
    def save_model(self, request, obj, form, change):
            obj.controller_by = request.user
            obj.save()
@admin.register(Controller)
class ControllerAdmin(admin.ModelAdmin):
    list_display = ['question','response']
    fields = ['finalist','question','response']
    list_filter =['controller_by','finalist','finalist__mission_configuration__mission','finalist__mission_configuration__school']
    search_fields = ['finalist','question']
    autocomplete_fields = ['finalist','question']
    def save_model(self, request, obj, form, change):
            obj.controller_by = request.user
            obj.save()
    
