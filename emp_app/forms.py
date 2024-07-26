from django import forms
from .models import Attendance, Employee


class AttendanceForm(forms.ModelForm):

    class Meta:
        model = Attendance
        # fields = '__all__'
        fields = ['employee', 'emp_date', 'in_time', 'out_time']
