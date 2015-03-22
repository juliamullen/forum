from django import forms
from conversation.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'text', 'date', 'image', 'conversation']

