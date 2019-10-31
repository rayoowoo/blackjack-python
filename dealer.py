from player import Player
import time

class Dealer(Player):
    def turn(self, deck):
        print("Dealer's turn")
        time.sleep(2)
        first = True

        while first or self.points() < 17:
            first = False
            print(f"Dealer's hand: {self.hand}")
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