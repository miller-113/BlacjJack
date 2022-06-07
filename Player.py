import abc
import random
import time

from const import MESSAGES, NAMES


class AbstractPlayer(abc.ABC):

    def __init__(self):
        self.cards = []
        self.bet = 0
        self.full_points = 0
        self.money = 1000
        self.name = None

    def change_points(self):
        self.full_points = sum([card.points for card in self.cards])
        for card in self.cards:
            if self.full_points > 21 and card.points == 11:
                self.full_points -= 10
                print('\nAce replaced 11 points to 1')

    def take_card(self, card):
        self.cards.append(card)
        self.change_points()

    @abc.abstractmethod
    def change_bet(self,  max_bet, min_bet):
        pass

    @abc.abstractmethod
    def ask_card(self):
        pass

    def print_cards(self):
        print('\n', self.name, " data")
        for card in self.cards:
            print(card, end='|')
        print('Full points: ', self.full_points)
        time.sleep(random.choice([0.5, 1, 2, 1.5, 1, 1.5]))


class Player(AbstractPlayer):

    def __init__(self):
        super(Player, self).__init__()
        self.name = 'Miller'

    def change_bet(self, max_bet, min_bet):
        while True:
            value = int(input('Make your bet: '))
            if max_bet > value > min_bet:
                self.bet = value
                self.money -= self.bet
                break
        print('Your bet is: ', self.bet)

    def ask_card(self):
        choice = input(MESSAGES.get('ask_card'))
        if choice == 'y':
            return True
        else:
            return False


class Bot(AbstractPlayer):

    def __init__(self):
        super().__init__()
        self.max_points = random.randint(17, 20)
        self.name = random.choice(NAMES)

    def change_bet(self, max_bet, min_bet):
        self.bet = random.randint(min_bet, max_bet)
        self.money -= self.bet
        print(self.name, 'give: ', self.bet)

    def ask_card(self):
        if self.full_points < self.max_points:
            return True
        else:
            return False


class Dealer(AbstractPlayer):

    def __init__(self):
        super(Dealer, self).__init__()
        self.name = 'Dealer'

    max_points = 17

    def change_bet(self, max_bet, min_bet):
        """
        NOTE: This type is Dealer so it has no bets
        """""
        raise Exception('This type is dealer so it has no bets')

    def ask_card(self):
        if self.full_points < self.max_points:
            return True
        else:
            return False
