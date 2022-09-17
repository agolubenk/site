from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import Post

class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
#    summernote_fields = ('content',)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}



admin.site.register(Post, PostAdmin)





