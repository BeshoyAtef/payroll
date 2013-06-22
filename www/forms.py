from django import forms
from www.models import CsvFile

class UploadForm(forms.Form): 
    file = forms.FileField() 
   