from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ('status',)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)

admin.site.site_header = 'MVMBlog'
admin.site.site_title = 'MVMBLog'
admin.site.index_title = 'MVMBlog'
