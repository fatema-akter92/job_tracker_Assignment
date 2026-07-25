from django import forms
from .models import JobApplication


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = [
            'company_name', 'position', 'job_location', 'salary',
            'status', 'application_date', 'deadline', 'notes',
        ]
        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'job_location': forms.TextInput(attrs={'class': 'form-control'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'application_date': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'}
            ),
            'deadline': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'}
            ),
            'notes': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 4}
            ),
        }

    def clean_company_name(self):
        company_name = self.cleaned_data.get('company_name', '').strip()
        if not company_name:
            raise forms.ValidationError("Company name is required.")
        return company_name

    def clean_position(self):
        position = self.cleaned_data.get('position', '').strip()
        if not position:
            raise forms.ValidationError("Position is required.")
        return position

    def clean_salary(self):
        salary = self.cleaned_data.get('salary')
        if salary is not None and salary < 0:
            raise forms.ValidationError("Salary cannot be negative.")
        return salary

    def clean_notes(self):
        notes = self.cleaned_data.get('notes', '')
        if notes and len(notes) > 500:
            raise forms.ValidationError("Notes cannot exceed 500 characters.")
        return notes

    def clean(self):
        cleaned_data = super().clean()
        application_date = cleaned_data.get('application_date')
        deadline = cleaned_data.get('deadline')
        if application_date and deadline:
            if deadline < application_date:
                raise forms.ValidationError(
                    "Deadline cannot be earlier than the application date."
                )
        return cleaned_data
