from django import forms
from .models import Post,Comment,Profile


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['username', 'post']
        widgets = {
            'myfield': forms.TextInput(attrs={'class': 'myfieldclass'}),
        }
