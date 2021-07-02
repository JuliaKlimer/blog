from .models import Post
from django.forms import ModelForm, TextInput, Textarea

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'post']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter title'
            }),
            'post': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter post'
            })
        }