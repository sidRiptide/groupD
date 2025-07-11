from django import forms

from Admin.models import Info


class InfoForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = '__all__'