from django import forms
from main.models import Application


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = [
            "military_unit",
            "automobile_type",
            "date_time",
            "route",
            "passengers_count",
            "comment",
            "file",
        ]

    def __init__(self, *args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)
        self.fields["comment"].required = False
        self.fields["file"].required = False

    def save(self, commit=True):
        instance = super(ApplicationForm, self).save(commit=False)
        if commit:
            instance.save()
        return instance
