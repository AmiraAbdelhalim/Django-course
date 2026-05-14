from django.contrib import admin
from .models import Task

# admin.site.register(Task)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'status', 'priority', 'due_date', 'owner'] #form
    list_display = ['title', 'status', 'priority', 'due_date', 'owner__email', 'created_at',] #table
    list_filter = ['status', 'priority', 'owner']
    search_fields = ['title']
 





