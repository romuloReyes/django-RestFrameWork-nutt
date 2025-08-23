from django.contrib import admin
# from django import forms
# from django_ckeditor_5.widgets import CKEditor5Widget

from .models import Category, Recipe, Heading

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('parent', 'name', 'title', 'slug')
    search_fields = ('name', 'title', 'description', 'slug')
    prepopulated_fields = {'slug':('name',)}
    list_filter = ('parent',)
    ordering = ('name',)
    readonly_fields=('id',)

class HeadingInline(admin.TabularInline):
    model=Heading
    extra=1
    fields=('title','level','order','slug')
    prepopulated_fields={'slug':('title',)}
    ordering=('order',)

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    # form = RecipeAdminForm
    list_display=('title', 'status', 'category', 'created_at', 'updated_at', 'slug')
    search_fields=('title', 'description', 'content', 'keywords', 'slug')
    prepopulated_fields={'slug':('title',)}
    list_filter=('status', 'category', 'updated_at',)
    ordering=('-created_at',)
    readonly_fields=('id', 'created_at', 'updated_at',)
    fieldsets=(
        ('General Information', {
            'fields':('title', 'description', 'content', 'thumbnail', 'keywords', 'category', 'slug')
        }),#Informacion general
        ('Status & Dates', {
            'fields':('status', 'created_at', 'updated_at')
        })
    )
    inlines=[HeadingInline]

# @admin.register(Heading)
# class HeadingAdmin(admin.ModelAdmin):
#     list_display=('title','recipe','level','order')
#     search_fields=('title','recipe__title')
#     list_filter=('level','recipe')
#     ordering=('recipe','order')
#     prepopulated_fields={'slug':('title',)}
