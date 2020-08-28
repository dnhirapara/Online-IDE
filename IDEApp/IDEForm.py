from django import forms
from .models import IDE


class Editor(forms.ModelForm):
    class Meta:
        model = IDE
        fields = ('title', 'code', 'inp',)
        widgets = {
            'code': forms.Textarea(attrs={'cols': 140, 'rows': 40, 'class': 'editor', 'required': 'False'}),
        }


# class Editor(forms.Form):
#     title = forms.CharField(max_length=20, initial="code1")
#     code = forms.CharField(widget=forms.Textarea, label="Code1")
#     inp = forms.SlugField()
