from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = '__all__'
        labels = {
            'full_name': 'Student Full Name',
            'national_id': 'National ID',
            'student_grade': 'Current Grade',
            'phone_number': 'Parent Phone Number',
            'from_school': 'Current School',
            'to_school': 'Requested School',
        }
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Enter full name'}),
            'national_id': forms.TextInput(attrs={'placeholder': '14-digit ID'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'e.g., 01012345678'}),
        }

    def validate_unique(self):
        # override default unique check (you already check it manually)
        pass
