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
        return [Player(i + 1) for i in range(int(number))]
    
    def set_points(self):
        for player in self.players:
            self.points[player] = 0
      
    def deal(self):
        for _ in [1, 2]:
            self.dealer.receive(self.deck.deal())
            for player in self.players:
                player.receive(self.deck.deal())

    def all_bets(self):
        print("\nBETTING PHASE")
        for player in self.players:
            player.place_bet()
            time.sleep(0.5)

    # Figure out game logic for multiple people playing at once.

    def one_round(self):
        self.set_points()
        self.all_bets()
        self.deal()
        self.all_turns()

    def all_turns(self):
        for player in self.players:
            self.player_turn(player)
        if max(self.points.values()) == -1:
            print("Everyone lost!")
        else:
            winners = []
            ties = []

            if self.dealer.turn(self.deck):
                winners = list(filter(lambda player: self.points[player] > 0, self.players))
            else:
                dealer_points = self.dealer.points()

                for player, points in self.points.items():
                    if points > dealer_points:
                        winners.append(player)
                    elif points == dealer_points:
                        ties.append(player)
                    else:
                        print(f"{player.name} has lost!")

        for winner in winners:
            winner.win_bet()
            print(f"{winner.name} has won!")
            time.sleep(0.5)

        for tie in ties:
            tie.push()
            print(f"{tie.name} has pushed.")
            time.sleep(0.5)           

    def player_turn(self, player):
        if player.turn(self.deck):
            self.points[player] = -1
        else:
            self.points[player] = player.points()

    def reset(self):
        self.bet = {
            1: 0,
            5: 0,
            25: 0
        }
        for player in self.players:
            player.reset()
        self.dealer.reset()

    def play_again(self):
        players = []
        for player in self.players:
            if player.valid():
                if input(f"{player.name}, do you still want to play? (y / n) \n>> ") == "y":
                    players.append(player)
        self.players = players
    
    def play_game(self):
        self.one_round()
        self.play_again()
        while len(self.players) > 0:
            self.reset()
            self.one_round()
            self.play_again()

        print("Thanks for playing")

BlackjackGame()