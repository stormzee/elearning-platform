from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        
        # 'class':'form-control',
        'placeholder':'comment here...',
        # 'id':'usercomment',
        'rows':'2'

    }))

# define the Meta ( the model for the 
# form u've created and the fields you wnt to receive from the user)
    class Meta:
        model = Comment
        fields = ('content',)