from Card import Card
import random


class Deck:
    def __init__(self):
        ranks = Card.accepted_ranks
        suits = Card.accepted_suits

        self.deck = [
            Card(suit, rank)
            for rank in ranks
            for suit in suits
        ]

    def shuffle(self):
        random.shuffle(self.deck)

    def print_deck(self):
        print("Deck size is", len(self.deck))
        print(".............")

        for card in self.deck:
            print(card)
            print("----------")

    def burn_card(self):
        self.deck.append(self.deck.pop(0))

    def give_card(self):
        return self.deck.pop(0)


if __name__ == "__main__":
    deck = Deck()
    deck.shuffle()

    print("Given card is:")
    card = deck.give_card()
    print(card)

    print("\nFull deck:")
    deck.print_deck()