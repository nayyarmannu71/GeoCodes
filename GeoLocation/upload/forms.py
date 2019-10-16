from django import forms
from upload.models import GeoFiles

class GeoFilesForm(forms.ModelForm):
    class Meta:
        model = GeoFiles
        fields = ('document', )