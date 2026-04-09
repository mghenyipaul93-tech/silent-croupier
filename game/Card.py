class Card:
    accepted_suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    accepted_ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10",
                      "Jack", "Queen", "King", "Ace"]

    def __init__(self, suit, rank):

        if not isinstance(suit, str) or not isinstance(rank, str):
            raise TypeError("Suit and rank must be strings")

        suit = suit.capitalize()
        rank = rank.capitalize()

        if suit not in Card.accepted_suits:
            raise ValueError("Invalid suit")

        if rank not in Card.accepted_ranks:
            raise ValueError("Invalid rank")

        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"


if __name__ == "__main__":
    c1 = Card("Hearts", "Ace")
    c2 = Card("Spades", "10")
    c3 = Card("Diamonds", "Jack")

    print(c1)
    print(c2)
    print(c3)