class Card():
    VALUES = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    SUITS = ["spades", "clubs", "diamonds", "hearts"]
    
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
