from django.contrib import admin
from .models import *
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "status", "date_created")
    list_filter = ("status",)
    search_fields = ['title', 'content', 'description']
    prepopulated_fields = {'slug':('title',)}


admin.site.register(Articles, ArticleAdmin)
admin.site.register(CalltoAction)
admin.site.register(Tags)
admin.site.register(Categories)
