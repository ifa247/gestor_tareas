from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Título de la tarea',
                'autofocus': 'autofocus'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Descripción (opcional)',
                'rows': 2,
                'cols': 40,
                'style': 'resize: vertical;'
            }),
        }
