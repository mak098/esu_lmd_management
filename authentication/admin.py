from django.contrib import admin
from .models import User,SchoolType,SchoolGroup,School,Role
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

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
    list_display = ('name',)
    fields = ('school_type','name','litera',)
    search_fields =('school_type__name','name','litera')
    autocomplete_fields =('school_type',)
    def save_model(self, request, obj, form, change):
            obj.created_by = request.user
            obj.save()
@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display =('code','acronym','name')
    fields = ('code','acronym','name','address','logo','school_group')
    search_fields =('school_group__name','name','acronym')
    list_filter = ('school_group__name','school_group__school_type__name',)
    autocomplete_fields =('school_group',)
    
    def save_model(self, request, obj, form, change):
            obj.created_by = request.user
            obj.save()