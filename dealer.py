from player import Player
import time
from chip import Chip
from hand import Hand

class Dealer(Player):
    def __init__(self):
        self.hand = Hand()
        self.chips = {
            1: [Chip(1), Chip(1), Chip(1), Chip(1), Chip(1)],
            5: [Chip(5), Chip(5), Chip(5), Chip(5), Chip(5)],
            25: [Chip(25)]
        }

    def turn(self, deck):
        print("Dealer's turn")
        time.sleep(2)
        first = True

        while first or self.points() < 17:
            first = False
            print(f"Dealer's hand: {self.hand} \nDealder's points: {self.points()}")
            time.sleep(2)
            self.receive(deck.deal())
        
        if self.points() > 21:
            print(f"Dealer's hand: {self.hand}")
            print(f"Dealer has busted with {self.points()} points.")
            return True
        else:
            print(f"Dealer has stood with {self.points()} points.")
            return False
        
        print("")