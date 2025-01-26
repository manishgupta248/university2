from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'code', 'category', 'type', 'cbcs_category', 'maximum_credit']

    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        # Customize form fields here if needed
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter course name'})
        self.fields['code'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter course code'})
        self.fields['category'].widget.attrs.update({'class': 'form-control'})
        self.fields['type'].widget.attrs.update({'class': 'form-control'})
        self.fields['cbcs_category'].widget.attrs.update({'class': 'form-control'})
        self.fields['maximum_credit'].widget.attrs.update({'class': 'form-control'})

