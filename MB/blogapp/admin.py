from django.contrib import admin

# Register your models here.
from blogapp.models import *

class ArticleAdmin(admin.ModelAdmin):
	# list_display = ['title', 'datetime', 'tags','content']
	class Media:
		js = (
			'/media/tinymce/tinymce.min.js',
			'/media/tinymce/textareas.js',
		)

admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag)
