class Card():
    def __init__(self, suit, rank):
        
        accepted_suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        accepted_ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

        if not isinstance(suit, str) or not isinstance(rank, str):
            raise TypeError("Suit and rank must be strings")
        
        suit = suit.capitalize()
        rank = rank.capitalize()

        if suit in accepted_suits:
            pass
        else:
            raise ValueError("Invalid suit")
        
        if rank in accepted_ranks:
            pass
        else:
            raise ValueError("Invalid rank")
        

        self.suit = suit
        self.rank = rank

        
    def print_card(self):
        print(f"{self.rank} of {self.suit}")

if __name__ == "__main__":
    card1 = Card("Hearts", "Ace")
    card2 = Card("Spades", "10")
    card3 = Card("Diamonds", "Jack")

    card1.print_card()
    card2.print_card()
    card3.print_card()
