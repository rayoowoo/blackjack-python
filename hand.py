from card import Card

class Hand():
    def __init__(self):
        self.cards = []
        self.points = 0
    
    def receive_card(self, card):
        self.cards.append(card)
        self.points = self.value()

    def value(self):
        sum = 0
        aces = 0
        for card in self.cards:
            if (card.value == "A"):
                aces += 1
            else:
                sum += card.point_value()
        
        ones = 0

        while (aces * 11 + sum > 21 and aces > 0):
            aces -= 1
            ones += 1
        
        return sum + ones + aces * 11

# hand = Hand()
# card1 = Card("6")
# card2 = Card("A")
# card3 = Card("5")
# card4 = Card("2")

# hand.receive_card(card1)
# print(hand.points)
# hand.receive_card(card2)
# print(hand.points)
# hand.receive_card(card3)
# print(hand.points)
# hand.receive_card(card4)
# print(hand.points)