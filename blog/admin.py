from django.contrib import admin
from .models import Blog , Category , Tag , Comment

# Register your models here.

#admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "date", "category")