from player import Player
from dealer import Dealer
from deck import Deck
from chip import Chip
import time

class BlackjackGame():
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.points = {}
        self.players = self.set_players()
        self.bet = {
            1: 0,
            5: 0,
            25: 0
        }
        self.play_game()

    def set_players(self):
        number = input("How many players (not including dealer)? \n>> ")
        players =  [Player(i + 1) for i in range(int(number))]
        for player in players:
            self.points[player] = None
        
        return players

        
    def deal(self):
        for _ in [1, 2]:
            self.dealer.receive(self.deck.deal())
            for player in self.players:
                player.receive(self.deck.deal())

    def place_bet(self, player):
        print(f"{player.name}, You have this many coins:")
        chips = player.all_chips()
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

        one_bet = valid_bet("one", one_amt) + self.bet[1]
        five_bet = valid_bet("five", five_amt) + self.bet[5]
        twenty_five_bet = valid_bet("twenty-five", twenty_five_amt) + self.bet[25]

        self.into_pot(player, one_amt, five_amt, twenty_five_amt)

        self.bet = {
            1: one_bet,
            5: five_bet,
            25: twenty_five_bet
        }

        print(f"{player.name} has placed a bet of {one_bet} one chips, {five_bet} five chips, and {twenty_five_bet} twenty-five chips. \n")
        time.sleep(0.5)

    def into_pot(self, player, one, five, twenty_five):
        for chip, amt in {1: one, 5: five, 25: twenty_five}.items():
            for _ in range(amt):
                player.chips[chip].pop()

    # TODO:
    # Figure out game logic for multiple people playing at once.
    def all_bets(self):
        print("\nBETTING PHASE")
        for player in self.players:
            self.place_bet(player)
        print(f"The pot is now {self.bet[1]} one chips, {self.bet[5]} five chips, and {self.bet[25]} twenty-five chips. \n")


    def one_round(self):
        self.all_bets()
        self.deal()
        self.all_turns()

    def all_turns(self):
        for player in self.players:
            self.player_turn(player)

    def player_turn(self, player):
        pass

    # def player_turn(self, player):
    #     if player.turn(self.deck):
    #         print("You lost!")
    #     elif self.dealer.turn(self.deck):
    #         print("You win!")
    #         self.win_bet(player)
    #     else:
    #         print(f"Player: {player.points()} points \nDealer: {self.dealer.points()} points")
    #         if player.points() < self.dealer.points():
    #             print("you lost!")
    #         else:
    #             print("You win!")
    #             self.win_bet(player)
    #     if player.valid() == False:
    #         self.players.remove(player)

    def win_bet(self, player):
        for chip, amt in self.bet.items():
            for _ in range(amt):
                player.chips[chip].append(Chip(chip))

    def reset(self):
        self.bet = {
            1: 0,
            5: 0,
            25: 0
        }
        for player in self.players:
            player.reset()
        self.dealer.reset()
    
    def play_game(self):
        self.one_round()
        while len(self.players) > 0:
            if input("Do you still want to play? (y / n) \n>> ") == "y":
                self.reset()
                self.one_round()
            else:
                break
        print("Thanks for playing")

BlackjackGame()