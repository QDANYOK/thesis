from django.shortcuts import render, redirect
from django.views import generic

from .forms import ImageForm
from .models import Puzzle


class PuzzleView(generic.ListView):
    template_name = 'apppuzzle/index.html'
    context_object_name = 'puzzle'


def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'apppuzzle/puzzles.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'apppuzzle/puzzles.html', {'form': form})