from django.forms import ModelForm
from MainApp.models import Snippet
from django.forms import ValidationError, Textarea, TextInput


class SnippetForm(ModelForm):
    class Meta:
        model = Snippet
        # Описываем поля, которые будем заполнять в форме
        fields = ['name', 'status', 'lang', 'code']
        labels = {"name": "", "status": "","lang": "", "code": ""}
        widgets = {
            "name": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Название сниппета",
                "style": "max-width: 300px"
            }),
            "code": Textarea(attrs={
                "placeholder": "Код сниппета",
                "rows": 5,
                "class": "input-lange",
                "style": "width: 50% !important; resize: vertical !important;"
            })
        }

    def clean_name(self):
        snippet_name = self.cleaned_data.get("name")
        if snippet_name is not None and len(snippet_name) > 3:
            return snippet_name
        raise ValidationError("Snippet's name too short.")
    
