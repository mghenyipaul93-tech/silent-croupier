from Deck import Deck
from Player import Player


class Game:

    def __init__(self):

        self.pot = 0

        self.deck = Deck()
        self.deck.shuffle()

        self.community_cards = []

        self.human = Player(
            type="human",
            cards=[self.deck.give_card(), self.deck.give_card()],
            total_bet_amount=0,
            name="Player",
            balance=1000
        )

        self.computer = Player(
            type="computer",
            cards=[self.deck.give_card(), self.deck.give_card()],
            total_bet_amount=0,
            name="Computer",
            balance=1000
        )

        self._turn = self.human

    
    @property
    def turn(self):
        return self._turn

    @turn.setter
    def turn(self, player):
        if isinstance(player, Player):
            self._turn = player
        else:
            raise ValueError("Turn must be a Player instance")

    
    def deal_flop(self):
        self.deck.burn_card()
        for _ in range(3):
            self.community_cards.append(self.deck.give_card())

    def deal_turn(self):
        self.deck.burn_card()
        self.community_cards.append(self.deck.give_card())

    def deal_river(self):
        self.deck.burn_card()
        self.community_cards.append(self.deck.give_card())

    def show_community_cards(self):
        print("\nCommunity Cards:")
        for card in self.community_cards:
            print(card)

    
    def find_rank(self, cards, rank):
        for card in cards:
            if card.rank == rank:
                return card
        return None

    
    def check_royal_flush(self, cards):

        royal_ranks = ["Ace", "King", "Queen", "Jack", "10"]
        found_cards = []

        for rank in royal_ranks:
            card = self.find_rank(cards, rank)
            if card:
                found_cards.append(card)
            else:
                return False

        suit = found_cards[0].suit

        for card in found_cards:
            if card.suit != suit:
                return False

        return True

   
    def check_winner(self):

        human_cards = self.human.cards + self.community_cards
        computer_cards = self.computer.cards + self.community_cards

        if self.check_royal_flush(computer_cards):
            return "computer"

        if self.check_royal_flush(human_cards):
            return "human"

        return None



if __name__ == "__main__":

    game = Game()

    print("\n--- GAME START ---\n")

    print("Computer cards:")
    for card in game.computer.cards:
        print(card)

    print("\nHuman cards:")
    for card in game.human.cards:
        print(card)