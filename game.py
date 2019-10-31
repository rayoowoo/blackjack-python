from player import Player
from dealer import Dealer
from deck import Deck
from chip import Chip

class BlackjackGame():
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
        self.bet = {
            1: 0,
            5: 0,
            25: 0
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
        twenty_five_amt = chips[25]

        def valid_bet(chip, amt):
            if amt == 0:
                return 0
                
            bet = int(input(f"How many {chip.upper()} chips do you want to bet? (Up to {amt}) \n>> "))
            while bet > amt or bet < 0:
                print(f"You don't have enough {chip.upper()} chips.")
                bet = int(input(f"How many {chip.upper()} chips do you want to bet? (Up to {amt}) \n>> "))
            
            return bet

        one_bet = valid_bet("one", one_amt)
        five_bet = valid_bet("five", five_amt)
        twenty_five_bet = valid_bet("twenty-five", twenty_five_amt)

        self.bet = {
            1: one_bet,
            5: five_bet,
            20: twenty_five_bet
        }

        print(f"You have placed a bet of {one_bet} one chips, {five_bet} five chips, and {twenty_five_bet} twenty-five chips. \n")
        time.sleep(0.5)

    def one_round(self):
        self.place_bet()
        self.deal()
        if self.player.turn(self.deck):
            print("You lost!")
            self.lose_bet()
        elif self.dealer.turn(self.deck):
            print("You win!")
            self.win_bet()
        else:
            print(f"Player: {self.player.points()} points \nDealer: {self.dealer.points()} points")
            if self.player.points() < self.dealer.points():
                print("you lost!")
                self.lose_bet()
            else:
                print("You win!")
                self.win_bet()

    def lose_bet(self):
        for chip, amt in self.bet.items():
            for _ in range(amt):
                self.player.chips[chip].pop()

    def win_bet(self):
        for chip, amt in self.bet.items():
            for _ in range(amt):
                self.player.chips[chip].append(Chip(chip))

    def reset(self):
        self.bet = {
            1: 0,
            5: 0,
            25: 0
        }
        self.player.reset()
        self.dealer.reset()
    
    def play_game(self):
        self.one_round()
        while self.player.valid():
            if input("Do you still want to play? (y / n) \n>> ") == "y":
                self.reset()
                self.one_round()
            else:
                break
        print("Thanks for playing")

BlackjackGame()