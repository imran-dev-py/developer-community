from django import forms
from . import models

class ProjectForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ('title', 'description', 'featured_image', 'demo_link', 'source_link', 'tags')

        widgets = {
            'tags': forms.CheckboxSelectMultiple(), 
        }
    