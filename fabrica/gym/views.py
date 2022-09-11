from django.shortcuts import render
from .models import Work

def my_fabric(request):
    work = Work.objects.all()
    works = {'work': work}
    return render(request, 'gym/index.html', works)