from django.forms import ModelForm

from apps.movies.models.comment import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
