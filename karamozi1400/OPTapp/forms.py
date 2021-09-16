from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField(label='محل آپلود فایل', widget=forms.FileInput(attrs={'class': 'form-control d-inline-block','id':'file','style':'width:500px;'}))
