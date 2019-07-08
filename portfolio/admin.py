from django.contrib import admin
from .models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields= ('created', 'updated')
    list_per_page = 10 

admin.site.register(Project, ProjectAdmin)