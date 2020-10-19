from django import forms
from .models import Category, Post, Comment
from martor.fields import MartorFormField


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','description','post_cover','categories','content')
        content = MartorFormField()
       

    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),            # give many to many field user friendly shape
        widget=forms.CheckboxSelectMultiple
    )

        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("content",)
        content = MartorFormField()


