from __future__ import unicode_literals
from django.contrib import admin
from .models import Comment, TreeDataFinal


class CommentAdmin(admin.ModelAdmin):
    list_display = ('treeID', 'comment_text', 'can_contact', 'contact_info', 'photo','approval',)
    list_editable = ('approval',)

class TreeAdmin(admin.ModelAdmin):
    list_display = ("id", "group_field", "leaf_fall", "name", "genus", "species_name", "family", "age_min", "age_max", "height_min", "height_max",)


admin.site.register(Comment, CommentAdmin)
admin.site.register(TreeDataFinal, TreeAdmin)