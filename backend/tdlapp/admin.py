from django.contrib import admin
from .models import Todo

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'completed', 'created_at')
    list_display_links = ('title',)
    list_editable = ('completed',)

    list_filter = ('completed', 'created_at')
    search_fields = ('title',)
    
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'