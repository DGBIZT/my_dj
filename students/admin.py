from django.contrib import admin
from .models import Student, Group
# Register your models here.

# admin.site.register(Student)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name', 'year',)
    list_filter = ('year', )
    search_fields = ('first_name', 'last_name')

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)
