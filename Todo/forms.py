from django import forms # type: ignore
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta: 
        model = Todo
        fields = ['title', 'task', 'dead_line']