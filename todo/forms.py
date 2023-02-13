from django import forms
from django.forms import ModelForm
from .models import Task


# Create your forms here.
class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'


