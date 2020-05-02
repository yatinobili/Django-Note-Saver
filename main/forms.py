from django.forms import ModelForm
from .models import Entry

class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ('name', 'text',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class' : 'input', 'placeholder' : 'Name'})
        self.fields['text'].widget.attrs.update({'class' : 'textarea', 'placeholder' : 'What\'s on your mind?'})