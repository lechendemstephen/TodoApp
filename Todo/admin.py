from django.contrib import admin # type: ignore
from .models import Todo
# Register your models here.

class TodoAdmin(admin.ModelAdmin): 
    list_display = ('title', 'task', 'dead_line')


admin.site.register(Todo, TodoAdmin)