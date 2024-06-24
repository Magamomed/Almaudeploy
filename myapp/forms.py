# myapp/forms.py

from django import forms
from .models import Application, Speciality
from .models import InterviewSchedule
from bootstrap_datepicker_plus.widgets import DatePickerInput
from .models import Event
from django.core.exceptions import ValidationError
from django import template





class InterviewScheduleForm(forms.ModelForm):
    class Meta:
        model = InterviewSchedule
        fields = ['date']
        widgets = {
            'date': DatePickerInput(options={
                "format": "YYYY-MM-DD",
                "useCurrent": True,
                "collapse": False,
            }),
        }

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = [
            'fio', 'city', 'school', 'student_class', 'phone', 'email',
            'telegram', 'instagram', 'parent_contacts', 'parent_fio',
            'specialties', 'language_kaz', 'language_rus', 'language_eng', 'university'
        ]
        widgets = {
            'fio': forms.TextInput(attrs={'placeholder': 'Введите ФИО'}),
            'city': forms.TextInput(attrs={'placeholder': 'Введите город'}),
            'school': forms.TextInput(attrs={'placeholder': 'Введите школу'}),
            'student_class': forms.TextInput(attrs={'placeholder': 'Введите класс'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Введите телефон'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Введите email'}),
            'telegram': forms.TextInput(attrs={'placeholder': 'Введите Telegram'}),
            'instagram': forms.TextInput(attrs={'placeholder': 'Введите Instagram'}),
            'parent_contacts': forms.TextInput(attrs={'placeholder': 'Введите контакты родителей'}),
            'parent_fio': forms.TextInput(attrs={'placeholder': 'Введите ФИО родителя'}),
            'specialties': forms.SelectMultiple(attrs={'placeholder': 'Выберите специальности', 'class': 'form-control'}),
            'language_kaz': forms.CheckboxInput(),
            'language_rus': forms.CheckboxInput(),
            'language_eng': forms.CheckboxInput(),
            'university': forms.TextInput(attrs={'placeholder': 'Введите университет'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Application.objects.filter(email=email).exists():
            raise ValidationError('Этот email уже используется.')
        return email



register = template.Library()

@register.filter(name='add_class')
def add_class(value, arg):
    return value.as_widget(attrs={'class': arg})

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'banner_image']