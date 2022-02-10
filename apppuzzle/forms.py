from django import forms

from apppuzzle.models import Puzzle


class PuzzleForm(forms.ModelForm):
    class Meta:
        model = Puzzle
        fields = ('image', 'title',)