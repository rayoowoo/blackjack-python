from chip import Chip
from hand import Hand

class Player():
    def __init__(self):
        self.hand = Hand()
        self.chips = {
            "one": [Chip(1), Chip(1), Chip(1), Chip(1), Chip(1)],
            "five": [Chip(5), Chip(5), Chip(5), Chip(5), Chip(5)],
            "ten": [Chip(10)],
            "twenty": [Chip(20)]
        }

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

        return {"one": len(self.chips["one"]), "five": len(self.chips["five"]), "ten": len(self.chips["ten"]), "twenty": len(self.chips["twenty"])}

# hi = Player()
# print(hi.all_chips())