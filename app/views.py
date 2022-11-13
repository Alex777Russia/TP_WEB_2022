from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET


def index(request):
    return render(request, 'index.html')

def question(request, question_id: int):
    return render(request, 'question.html')

def new_question(request):
    return render(request, 'new_question.html')

def tag_question(request):
    return render(request, 'tag_question.html')

def settings(request):
    return render(request, 'settings.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')
