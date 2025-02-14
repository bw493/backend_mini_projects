from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['character', 'comment_text']
        widgets = {
            'character': forms.Select(attrs={'class': 'form-control'}),
            'comment_text': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }