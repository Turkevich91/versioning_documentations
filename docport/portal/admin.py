from django.contrib import admin
from .models import Article, Comment


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_at')
    search_fields = ('title', 'content')
    list_filter = ('published_at',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('article', 'author', 'created_at')
    search_fields = ('text',)
    list_filter = ('created_at',)
