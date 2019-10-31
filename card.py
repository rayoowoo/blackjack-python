class Card():
    VALUES = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    SUITS = ["spades", "clubs", "diamonds", "hearts"]
    COUNTS = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 10,
        "Q": 10,
        "K": 10,
            }

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def point_value(self):
        return Card.COUNTS[self.value]