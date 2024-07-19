from django.forms import CheckboxInput
from django import forms


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if hasattr(field.widget, 'attrs') and not isinstance(field.widget, CheckboxInput):
                field.widget.attrs['class'] = 'form-control'


class CityForm(forms.Form, StyleFormMixin):
    city = forms.CharField(label='Город', max_length=100, help_text='Введите название города')
