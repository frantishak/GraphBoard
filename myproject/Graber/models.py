import requests
from .secret_date.auth import *
from django.db import models


class Card(models.Model):
    # Fields
    id_card = models.CharField(max_length=50, primary_key=True)
    name_card = models.CharField(max_length=20)
    constructor_card = models.ForeignKey('Constructor', on_delete=models.CASCADE)
    due_card = models.DateTimeField()
    color_card = models.CharField(max_length=10)
    list_card = models.ForeignKey('List', on_delete=models.CASCADE)

    def __str__(self):
        return self.name_card

    def get_id_list(id_board, name_list):

        url = "https://api.trello.com/1/boards/{id}/lists?fields=id,name&key={key}&token={token}".format(id=id_board, key=my_key, token=GraphBoard)
        respons = requests.get(url)
        respons = respons.json()
        for element in respons:
            if element['name'] == name_list:
                id_list = element['id']
                return id_list, name_list

        return None

    def get_detail_card(id_list):

        url = "https://api.trello.com/1/lists/{id}/cards?fields=id,name,due&key={key}&token={token}".format(id=id_list, key=my_key, token=GraphBoard)
        respons = requests.get(url)
        respons = respons.json()

        for elem in respons:
            card_id = elem['id']
            card_name = elem['name']
            card_due = elem['due']

        return card_id, card_name, card_due

    def get_members_card(id_card):
        result = []

        url = "https://api.trello.com/1/cards/{id}/members?fields=username&key={key}&token={token}".format(id=id_card, key=my_key, token=GraphBoard)
        respons = requests.get(url)
        respons = respons.json()
        for elem in respons:
            i = elem['username']
            result.append(i)

        return result



class Constructor(models.Model):

    def __str__(self):
        return self.constructor_name

    constructor_name = models.CharField(max_length=20)


class List(models.Model):

    def __str__(self):
        return self.list_name

    list_name = models.CharField(max_length=20)
