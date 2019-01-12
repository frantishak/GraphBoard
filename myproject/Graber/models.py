import requests
from .secret_date.auth import *
from django.db import models


class Card(models.Model):
    # Fields
    id_card = models.CharField(max_length=50, primary_key=True)
    name_card = models.CharField(max_length=20)
   # constructor_card = models.ForeignKey('Constructor', on_delete=models.CASCADE)
    due_card = models.DateTimeField(auto_now=True)
   # color_card = models.CharField(max_length=10)
    #list_card = models.ForeignKey('List', on_delete=models.CASCADE)

    def __str__(self):
        return self.name_card

    def create_card(id_card,name_card,due_card):

        new_card = Card(id_card=id_card,name_card=name_card,due_card=due_card)
        new_card.save()

    def get_id_list(id_board, name_list):

        url = "https://api.trello.com/1/boards/{id}/lists?fields=id,name&key={key}&token={token}".format(id=id_board, key=my_key, token=my_token)
        respons = requests.get(url)
        respons = respons.json()
        for element in respons:
            if element['name'] == name_list:
                id_list = element['id']
                return id_list

        return None

    def get_cards(id_list):

        url = "https://api.trello.com/1/lists/{id}/cards?fields=id,name,due&key={key}&token={token}".format(id=id_list, key=my_key, token=my_token)
        respons = requests.get(url)
        cards_list = respons.json()

        for card in cards_list:
            id_card = card['id']
            name_card = card['name']
            if card['due'] == 'None':
                due_card = 'NULL'
            due_card = card['due']
            new_card = Card(id_card=id_card, name_card=name_card, due_card=due_card)
            new_card.save()


    def get_members_card(id_card):
        result = []

        url = "https://api.trello.com/1/cards/{id}/members?fields=username&key={key}&token={token}".format(id=id_card, key=my_key, token=my_token)
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
