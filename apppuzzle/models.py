from django.db import models


class Puzzle(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='photo/')

    def __str__(self):
        return self.title
