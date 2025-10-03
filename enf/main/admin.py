from django.contrib import admin
from . models import Post,Comment

# Register your models here.
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

class AdminPost(admin.ModelAdmin):
    list_display = ('title','data')
    inlines = [CommentInline]

admin.site.register(Post,AdminPost)

class AdminComment(admin.ModelAdmin):
    list_display = ('author')

admin.site.register(Comment)
