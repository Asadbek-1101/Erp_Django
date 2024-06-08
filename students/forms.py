from django import forms

class HomeworkFrom(forms.Form):
       description = forms.CharField(widget=forms.Textarea)
       homework_file = forms.FileField(widget=forms.FileInput)
