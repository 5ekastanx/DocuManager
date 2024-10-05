from django.contrib import admin
from apps.contents.models import Document, Folder


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'user', 'created_at', 'updated_at', 'is_active', 'extension', 'size')
    list_filter = ('is_active', 'user', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('user', 'folder', 'file', 'name', 'description', 'is_active', 'extension', 'size')
        }),
        ('Access', {
            'fields': ('access',)
        }),
        ('Dates', {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )


@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'created_at', 'updated_at', 'is_active')
    list_filter = ('is_active', 'user', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('user', 'name', 'description', 'is_active')
        }),

        ('Dates', {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        }),
    )