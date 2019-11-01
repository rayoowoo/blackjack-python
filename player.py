from chip import Chip
from hand import Hand
import random

class Player():
    def __init__(self, number):
        self.name = input(f"Player {number}, what is your name? \n>> ")
        self.hand = Hand()
        self.chips = {
            1: [Chip(1), Chip(1), Chip(1), Chip(1), Chip(1)],
            5: [Chip(5), Chip(5), Chip(5), Chip(5), Chip(5)],
            25: [Chip(25)]
        }
        self.bet = {
            1: 0,
            5: 0,
            25: 0
        }
    
    def place_bet(self):
        print(f"{self.name}, You have this many coins:")
        chips = self.all_chips()
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
        twenty_five_bet = valid_bet("twenty_five", twenty_five_amt)

        self.into_pot(one_bet, five_bet, twenty_five_bet)

        print(f"{self.name} has placed a bet of {one_bet} one chips, {five_bet} five chips, and {twenty_five_bet} twenty-five chips. \n")

    def into_pot(self, one, five, twenty_five):
        for chip, amt in {1: one, 5: five, 25: twenty_five}.items():
            for _ in range(amt):
                self.chips[chip].pop()

        self.bet = {
            1: one,
            5: five,
            25: twenty_five
        }

    def win_bet(self):
        self.push()
        self.push()

    def push(self):
        for chip, amt in self.bet.items():
            for _ in range(amt):
                self.chips[chip].append(Chip(chip))

    def valid(self):
        for amt in self.chips.values():
            if len(amt) > 0:
                return True
        return False

    def receive(self, card):
        self.hand.receive_card(card)

    def points(self):
        return self.hand.points

    def all_chips(self):
        list_of_chips = []
        for chip in self.chips.values():
            list_of_chips += chip

        list_of_chips = list(map(lambda chip: chip.value, list_of_chips))
        print(list_of_chips)

        return {1: len(self.chips[1]), 5: len(self.chips[5]), 25: len(self.chips[25])}

    def turn(self, deck):
        done = False
        print(f"{self.name}'s turn")

        while done == False:
            print(f'Your hand: {self.hand} \nYour points: {self.points()}')
            action = input("Hit or stand? (h / s) \n>> ")
            if action is "h":
                self.receive(deck.deal())
                if self.points() > 21:
                    done = True
                    print(f'Your hand: {self.hand}')
                    print(f"You have busted with {self.points()} points!")
                    return True
            elif action is "s":
                print(f"{self.name} have decided to stand. You have {self.points()} points.")
                done = True
            else:
                print("Invalid input. Try again.")
        
        print("")
        return False

    def reset(self):
        self.hand = Hand()

# hi = Player()
# print(hi.all_chips())