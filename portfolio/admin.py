# portfolio/admin.py

from django.contrib import admin
from .models import Project, Skill, Contact, Experience, Education

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'featured', 'created_at']
    list_filter = ['featured', 'created_at']
    search_fields = ['title', 'description']
    list_editable = ['featured']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency']
    list_filter = ['category']
    list_editable = ['proficiency']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'is_read']
    list_filter = ['is_read', 'created_at']
    readonly_fields = ['name', 'email', 'subject', 'message', 'created_at']
    list_editable = ['is_read']

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'start_date', 'is_current']
    list_filter = ['is_current']

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'institution', 'start_date', 'is_current']
    list_filter = ['is_current']