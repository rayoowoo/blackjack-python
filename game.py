from player import Player
from dealer import Dealer
from deck import Deck

class BlackjackGame():
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = {
            1: 0,
            5: 0,
            10: 0,
            20: 0
        }
        self.play_game()
        
    def deal(self):
        self.dealer.receive(self.deck.deal())
        self.player.receive(self.deck.deal())
        self.dealer.receive(self.deck.deal())
        self.player.receive(self.deck.deal())

    # TODO:
    # figure out game logic

    # player places bet - done
    # deal - done
    # player goes first. - done
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
        print("")

        one_amt = chips[1]
        five_amt = chips[5]
        ten_amt = chips[10]
        twenty_amt = chips[20]

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
            1: one_bet,
            5: five_bet,
            10: ten_bet,
            20: twenty_bet
        }

        print(f"You have placed a bet of {one_bet} one chips, {five_bet} five chips, {ten_bet} ten chips, and {twenty_bet} twenty chips. \n")

    def one_round(self):
        self.place_bet()
        self.deal()
        if self.player.turn(self.deck):
            print("You lost!")
        else:
            if self.dealer.turn(self.deck):
                print("You win!")
            else:
                print(f"Player: {self.player.points()} points \nDealer: {self.dealer.points()} points")

    def lose_bet(self):
        for chip, amt in self.bet.items():
            for _ in amt:
                self.player.chips[chip].pop()
    
    def play_game(self):
        self.one_round()
        

BlackjackGame()