from django.contrib import admin
from models import ErrorRe,FileList,Comment
# Register your models here.

@admin.register(ErrorRe)
class ErrorReAdmin(admin.ModelAdmin):
    list_display = ('id','ErrorRes')

@admin.register(FileList)
class ErrorReAdmin(admin.ModelAdmin):
    list_display = ('name','path','tat')

@admin.register(Comment)
class ErrorReAdmin(admin.ModelAdmin):
    list_display = ('id','comment','grade','create_man','create')



