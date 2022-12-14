from django.db import models

class SudokuFront(models.Model):
    grid = models.IntegerField()


    def __str__(self):
        return self.grid
