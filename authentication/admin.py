from django.contrib import admin
from .models import User,SchoolType,SchoolGroup,School,Role
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

class SchoolInline(admin.TabularInline):
	
    model = School
    extra = 0
    fields = ('code','acronym','name','address','logo','school_group')
    def save_related(self, request, obj, form, change):
        obj.created_by = request.user
        obj.save()
@admin.register(User)
class UserAdmin(DjangoUserAdmin):

    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    fieldsets = (
        ('identifier', {
            'fields': ('username', 'password'),
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email'),
        }),
        
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser','school_group','role', 'groups'),
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined'),
        })
    )
    filter_horizontal =('school_group','role','groups')

@admin.register(SchoolType)
class SchoolTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fields =('name',)
    search_fields = ('name',) 
@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fields =('name',)
    search_fields = ('name',) 
    
@admin.register(SchoolGroup)
class SchoolGroupAdmin(admin.ModelAdmin):
    list_display = ('name','litera')
    fields = ('school_type','name','litera',)
    search_fields =('school_type__name','name','litera')
    autocomplete_fields =('school_type',)
    list_filter =['school_type']
    inlines =[SchoolInline,]
    def save_model(self, request, obj, form, change):
            obj.created_by = request.user
            obj.save()
    
    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            # Mettre à jour le champ created_by avec l'utilisateur actuel
            instance.created_by = request.user
            instance.save()
        formset.save_m2m()
@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display =('created_by','code','acronym','name')
    fields = ('code','acronym','name','address','logo','school_group')
    search_fields =('school_group__name','name','acronym')
    list_filter = ('school_group__school_type','school_group','address')
    autocomplete_fields =('school_group',)
    
    def save_model(self, request, obj, form, change):
            obj.created_by = request.user
            obj.save()