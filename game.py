from player import Player
from deck import Deck

class BlackjackGame():
    def __init__(self):
        self.deck = Deck()
        self.dealer = Player()
        self.player = Player()
        self.pot = []
        
    def deal(self):
        self.dealer.receive(self.deck.deal())
        self.player.receive(self.deck.deal())
        self.dealer.receive(self.deck.deal())
        self.player.receive(self.deck.deal())

    # figure out game logic

    # player places bet
    # deal
    # player goes first. 
        # can choose to receive another card, "hit", or "stand", and receive no cards. 
    # dealer goes second.
        # must hit until 17 or higher. then they must stand. 
    
    # if the player busts, money goes into the pot. 
    # if dealer busts, the player with closest to 21 (or 21) wins the pot (usually multiple people). for this game, we'll just double the winnings. 
    # if nobody busts, player with score closest to 21 wins. 

    # the round keeps going until either the player loses all their money, or the player decides to quit. 

    def place_bet(self, amount):
        print("You have this many coins:")
        print(coin.value for coin in self.player.coins)