from django.contrib import admin
from webapps.models import Student
class StudentAdmin(admin.ModelAdmin):
	list_display=['no','name','mobile','city','course']
admin.site.register(Student,StudentAdmin)
# Register your models here.
