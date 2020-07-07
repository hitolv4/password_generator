from django.shortcuts import render
from django.http import HttpResponse
import random
import string

# Create your views here.


def home(request):
    return render(request, 'generator/home.html')


def generated_password(request):
    character = list(string.ascii_lowercase)
    length = int(request.GET.get('length'))
    if request.GET.get('uppercase'):
        character.extend(list(string.ascii_uppercase))
    if request.GET.get('numbers'):
        character.extend(list(string.digits))
    if request.GET.get('special'):
        character.extend(list(string.punctuation))
    context = {
        'password': ''.join(
            [random.choice(character) for i in range(length)]
        )
    }

    return render(request, 'generator/password.html', context)


def about(request):
    return render(request, 'generator/about.html')
