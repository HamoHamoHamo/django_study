from django.contrib import admin
from .models import Tag, Post, Comment, Reply
from django.utils.safestring import mark_safe
from .models import Post

class ReplyInline(admin.StackedInline):
    model = Reply
    extra = 5

class CommentAdmin(admin.ModelAdmin):
    inlines = [ReplyInline]

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_public', 'updated_at', 'created_at', 'title_len']
    ordering = ('-created_at',)
    list_filter = ['is_public', 'tags']
    search_fields = ('title', 'text')

    def thumbnail_preview(self, obj):
        return mark_safe('<img src="{}" style="width:100px; height:auto;">'.format(obj.thumbnail.url))
    
    thumbnail_preview.short_description = '프리뷰'

    def title_len(self, obj):
        return len(obj.title)

    title_len.short_description = '제목글자수'

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Reply)
admin.site.register(Tag)

# Register your models here.