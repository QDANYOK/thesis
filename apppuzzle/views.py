from django.shortcuts import render, redirect
from django.views import generic

from .forms import PuzzleForm
from .models import Puzzle


class PuzzleView(generic.ListView):
    template_name = 'apppuzzle/puzzles.html'
    context_object_name = 'puzzle'

    def get_queryset(self):
        return PuzzleForm


def post_new(request):
    if request.method == "POST":
        form = PuzzleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('apppuzzle/index.html')
    else:
        form = PuzzleForm()
    return render(request, 'apppuzzle/index.html', {'form': form})
