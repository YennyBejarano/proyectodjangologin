from django.forms import ModelForm
from .models import task


class taskform(ModelForm):
    class Meta:
        model = task
        fields = ['title', 'description', 'important', ]