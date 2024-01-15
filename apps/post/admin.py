from django.contrib import admin
from apps.post.models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    model = Task
    list_display = ('title', 'description', 'created_at', 'due_date', 'status', 'user')
    list_filter = ('title', 'status')
    search_fields = ('title','due_date',)  # Замените 'title' на ('title',)
    extra = 1
