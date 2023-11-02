import time
import random

class Card:

    NumList = ['Joker', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dama', 'King', 'Tyz']
    MastList = ['пик', 'бубей', 'крестей', 'червей']

    def __init__(self, i, j):
        self.mastB = self.MastList[i-1]
        self.numB = self.NumList[j-1]

class DeckOfCards:

    def __init__(self):
        self.deck = [None] * 56
        k = 0
        for i in range(1, 5):
            for j in range(1, 15):
                self.deck[k] = Card(i, j)
                k += 1

    def shuffle(self):
        random.shuffle(self.deck)

    def get(self, i):
        if 0 <= i <= 55:
            answer = f'{self.deck[i].numB} {self.deck[i].mastB}'
        else:
            answer = 'Такой карты нет'
        return answer

deck = DeckOfCards()
deck.shuffle()
n = int(input('Выбери карту:   '))
try:
    if 0 <= n <= 55:
        print(f' Вы взяли {deck.get(n)}')
    else:
        print('Такой карты нет')
except:
    print('Такой карты нет')