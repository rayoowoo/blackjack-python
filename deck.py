from card import Card
import random

class Deck():
    def __init__(self):
        self.cards = self.create_deck()
        self.shuffle()
    
    def create_deck(self):
        deck = []
        for value in Card.VALUES:
            for suit in Card.SUITS:
                deck.append(Card(value, suit))
        return deck

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

    def reset(self):
        self.cards = self.create_deck()
        self.shuffle()