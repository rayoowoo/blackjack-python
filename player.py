from chip import Chip
from hand import Hand

class Player():
    def __init__(self):
        self.hand = Hand()
        self.money = [
            Chip(5), Chip(5), Chip(5), Chip(5), Chip(5), Chip(10), Chip(20)
        ]

    def receive(self, card):
        self.hand.receive_card(card)

    def points(self):
        return self.hand.points