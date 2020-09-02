from django.contrib import admin
from .models import Teacher, Notice , Assignment
from django.contrib.admin.options import ModelAdmin


# Register your models here.
class TeacherAdmin(ModelAdmin):
	list_display = ['name', 'qualification', 'phonenumber']
	search_field = ['name']
	list_filter = ['salary', 'qualification']

admin.site.register(Teacher, TeacherAdmin)

class NoticeAdmin(ModelAdmin):
	list_display = ['title', 'author','published']
	search_field = ['name', 'author', 'published']
	list_filter = ['title', 'published']

admin.site.register(Notice, NoticeAdmin)

class AssignmentAdmin(ModelAdmin):
	list_display = ['title', 'subject', 'section', 'branch', 'published']
	search_field = [ 'title', 'subject', 'section', 'branch',]
	list_filter = [ 'title', 'subject', 'section', 'branch', 'published']

admin.site.register(Assignment, AssignmentAdmin)

"""
class PostAdmin(ModelAdmin):
	list_display = ['posttitle', 'postauthor','postpublished']
	search_field = ['posttitle', 'postauthor']
	list_filter = ['posttitle', 'postpublished', 'postauthor']

admin.site.register(Post, PostAdmin)"""
