from player import Player
from deck import Deck

class BlackjackGame():
    def __init__(self):
        self.deck = Deck()
        self.dealer = Player()
        self.player = Player()
        
    def deal(self):
        self.dealer.receive(self.deck.deal())
        self.player.receive(self.deck.deal())
        self.dealer.receive(self.deck.deal())
        self.player.receive(self.deck.deal())

    # figure out game logic
    