from player import Player
from deck import Deck

class BlackjackGame():
    def __init__(self):
        self.deck = Deck()
        self.dealer = Player()
        self.player = Player()
        self.pot = []
        self.bet = {
            "one": 0,
            "five": 0,
            "ten": 0,
            "twenty": 0
        }
        
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

    def place_bet(self):
        print("You have this many coins:")
        chips = self.player.all_chips()

        one_amt = chips['one']
        five_amt = chips['five']
        ten_amt = chips['ten']
        twenty_amt = chips['twenty']

        def valid_bet(chip, amt):
            bet = int(input(f"How many {chip.upper()} chips do you want to bet? (Up to {amt}) \n>> "))
            while bet > amt or bet < 0:
                print(f"You don't have enough {chip.upper()} chips.")
                bet = int(input(f"How many {chip.upper()} chips do you want to bet? (Up to {amt}) \n>> "))
            
            return bet

        one_bet = valid_bet("one", one_amt)
        five_bet = valid_bet("five", five_amt)
        ten_bet = valid_bet("ten", ten_amt)
        twenty_bet = valid_bet("twenty", twenty_amt)

        self.bet = {
            "one": one_bet,
            "five": five_bet,
            "ten": ten_bet,
            "twenty": twenty_bet
        }

        print(f"You have placed a bet of {one_bet} one chips, {five_bet} five chips, {ten_bet} ten chips, and {twenty_bet} twenty chips.")



game = BlackjackGame()
game.place_bet()