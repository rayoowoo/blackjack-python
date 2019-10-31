from chip import Chip
from hand import Hand

class Player():
    def __init__(self):
        self.hand = Hand()
        self.chips = {
            1: [Chip(1), Chip(1), Chip(1), Chip(1), Chip(1)],
            5: [Chip(5), Chip(5), Chip(5), Chip(5), Chip(5)],
            10: [Chip(10)],
            20: [Chip(20)]
        }

    def valid(self):
        for amt in self.chips.values():
            if len(amt) > 0:
                return True
        return False

    def receive(self, card):
        self.hand.receive_card(card)

    def points(self):
        return self.hand.points

    def all_chips(self):
        list_of_chips = []
        for chip in self.chips.values():
            list_of_chips += chip

        list_of_chips = list(map(lambda chip: chip.value, list_of_chips))
        print(list_of_chips)

        return {1: len(self.chips[1]), 5: len(self.chips[5]), 10: len(self.chips[10]), 20: len(self.chips[20])}

    def turn(self, deck):
        done = False
        print("Player's turn")

        while done == False:
            print(f'Your hand: {self.hand} \nYour points: {self.points()}')
            action = input("Hit or stand? (h / s) \n>> ")
            if action is "h":
                self.receive(deck.deal())
                if self.points() > 21:
                    done = True
                    print(f'Your hand: {self.hand}')
                    print(f"You have busted with {self.points()} points.")
                    return True
            elif action is "s":
                print(f"You have decided to stand. You have {self.points()} points.")
                done = True
            else:
                print("Invalid input. Try again.")
        
        print("")
        return False

    def reset(self):
        self.hand = Hand()

# hi = Player()
# print(hi.all_chips())