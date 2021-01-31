from django import forms

class URLForm(forms.Form):
    longurl = forms.URLField(max_length=250)
    custom_name = forms.CharField(max_length = 30, required = False)