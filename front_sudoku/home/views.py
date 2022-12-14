from django.shortcuts import render
from django.http import HttpResponse
from .models import SudokuFront

def index(request):
    sudoku = SudokuFront.objects.all()
    data = {'sudoku' : sudoku}
    return render(request,'home/index.html', data)
