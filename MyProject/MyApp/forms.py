from django import forms
from .models import ExampleModel


class ExampleForm(forms.ModelForm):
    class Meta:
        model = ExampleModel
        fields = ['name', 'email', 'message']
        labels = {
            'name': 'Имя',
            'email': 'Электронная почта',
            'message': 'Сообщение',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }
