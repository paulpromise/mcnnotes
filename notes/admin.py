from django.contrib import admin
from .models import Note, Subject


# Register your models here.
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'note_count')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    ordering = ('name',)
    
    def note_count(self, obj):
        return obj.notes.count()
    note_count.short_description = 'Number of Notes'

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'subject', 'user', 'created_at', 'updated_at')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content', 'subject__name')
    list_filter = ('created_at', 'updated_at', 'user', 'subject')
    ordering = ('-created_at',)
    raw_id_fields = ('user',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'subject', 'user')
        }),
        ('Content', {
            'fields': ('content',),
            'classes': ('wide',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )