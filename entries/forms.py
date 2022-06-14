from django import forms
from .models import Entry

class EntryForm(forms.ModelForm):
    class Meta :
        model = Entry
        exclude = ('date_created',)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Title Heading',
            'content': 'Add subject',
        }
        self.fields['title'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].widget.attrs['placeholder'] = placeholders[field]
            