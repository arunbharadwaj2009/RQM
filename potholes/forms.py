from django import forms
from .models import JsonFile


class JsonFileForm(forms.ModelForm):
    class Meta:
        model = JsonFile
        fields = ["jsonfile"]
