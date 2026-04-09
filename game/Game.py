from Deck import Deck
from Player import Player


class Game():

    def __init__(self):

        self.pot = 0

        self.deck = Deck()
        self.deck.shuffle()

        human_cards = [self.deck.give_card(), self.deck.give_card()]
        computer_cards = [self.deck.give_card(), self.deck.give_card()]

        self.human = Player(
            type="human",
            cards=human_cards,
            total_bet_amount=0,
            name="Player",
            balance=1000
        )

        self.computer = Player(
            type="computer",
            cards=computer_cards,
            total_bet_amount=0,
            name="Computer",
            balance=1000
        )

        self._turn = self.human   # keep your turn system

    @property
    def turn(self):
        return self._turn

    @turn.setter
    def turn(self, player):

        if isinstance(player, Player):
            self._turn = player
        else:
            raise ValueError("Turn must be set to a Player instance.")


if __name__ == "__main__":
    game = Game()

    print("Human cards:", [str(c) for c in game.human.cards])
    print("Computer cards:", [str(c) for c in game.computer.cards])