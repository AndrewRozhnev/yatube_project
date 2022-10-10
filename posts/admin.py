from django.contrib import admin

from .models import Group, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'pub_date', 'author', 'group')
    list_editable = ('group',)
    search_fields = ('text',)
    list_filter = ('pub_date',)

    empty_value_display = '-empty-'


@admin.register(Group)
class PostGroup(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'slug')
