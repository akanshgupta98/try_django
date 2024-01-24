from django import forms
from blog.models import BlogPost


class BlogPostForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)
    date = forms.DateField(required=False)
    slug = forms.SlugField()

class BlogPostModelForm(forms.ModelForm):
    date = forms.DateField(required=False)
    class Meta:
        model = BlogPost
        fields = ['title','content','slug']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.PasswordInput()