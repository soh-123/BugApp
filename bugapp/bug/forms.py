from django import forms
from .models import Bug

class BugForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ['bug_description', 'bug_type', 'report_date', 'status']
