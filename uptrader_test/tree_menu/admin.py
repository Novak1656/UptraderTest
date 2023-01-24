from django.contrib import admin
from .models import Menu, MenuCategories


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'category', 'link', 'parent',)
    list_display_links = ('pk', 'name',)


@admin.register(MenuCategories)
class MenuCategoriesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'systemic_name',)
    list_display_links = ('pk', 'name',)
