from django import forms

from apppuzzle.models import Puzzle


class ImageForm(forms.ModelForm):
    class Meta:
        model = Puzzle
        fields = ('title', 'image',)