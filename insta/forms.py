from django import forms
from .models import Post,Comment,Profile


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['username', 'post']
        widgets = {
            'myfield': forms.TextInput(attrs={'class': 'myfieldclass'}),
        }
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude=['username','post_date','likes','p_pic']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic','bio','email']
