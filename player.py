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

    def receive(self, card):
        self.hand.receive_card(card)

    def points(self):
        return self.hand.points

    def all_chips(self):
        list_of_chips = []
        for chip in self.chips.values():
            list_of_chips += chip

        return list(map(lambda chip: chip.value, list_of_chips))

# hi = Player()
# print(hi.all_chips())