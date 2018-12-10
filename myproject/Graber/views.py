from django.http import HttpResponse
from django.shortcuts import render
from .models import Card

def index(request):
    i = Card.name_card('RE0MJmeD')

    return HttpResponse(i)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)