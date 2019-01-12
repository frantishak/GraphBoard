from django.http import HttpResponse
from .models import Card
from .secret_date.auth import id_board, names_lists, id_list

def index(request):
    Card.get_cards(id_list)
    i = Card.objects.all()

    return HttpResponse(i)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)