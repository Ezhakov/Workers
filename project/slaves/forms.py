from django import forms

from project.slaves import models


class ResumeForms(forms.ModelForm):
    class Meta:
        model = models.Resume
        exclude = ('owner', 'registered_in', )