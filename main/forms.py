from .models import Task
from django.forms import ModelForm, TextInput, Textarea, CheckboxInput


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'task', 'isDone']
        widgets = {
            'title': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите название'}
            ),
            'task': Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите описание задачи'}
            ),
            'isDone': CheckboxInput(attrs={'class': 'form-check-input'})
        }