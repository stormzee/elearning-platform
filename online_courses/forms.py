from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        
        'class':'form-control',
        'placeholder':'Type your comment',
        'id':'usercomment',
        'rows':'4'

    }))

# define the Meta ( the model for the 
# form u've created and the fields you wnt to receive from the user)
    class Meta:
        model = Comment
        fields = ('content',)