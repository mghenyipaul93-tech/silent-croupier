from Deck import Deck
from Player import Player
from collections import Counter


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

    # DEALING
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

    # HELPERS
    def get_values(self, cards):
        rank_value = {
            "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
            "7": 7, "8": 8, "9": 9, "10": 10,
            "Jack": 11, "Queen": 12, "King": 13, "Ace": 14
        }
        return [rank_value[c.rank] for c in cards]

    def get_suits(self, cards):
        return [c.suit for c in cards]

    # HAND CHECKS
    def is_flush(self, cards):
        return max(Counter(self.get_suits(cards)).values()) >= 5

    def is_straight(self, cards):
        values = sorted(set(self.get_values(cards)))
        for i in range(len(values) - 4):
            if values[i:i+5] == list(range(values[i], values[i] + 5)):
                return True
        return False

    def is_four_kind(self, cards):
        return 4 in Counter(self.get_values(cards)).values()

    def is_three_kind(self, cards):
        return 3 in Counter(self.get_values(cards)).values()

    def is_pair(self, cards):
        return list(Counter(self.get_values(cards)).values()).count(2) >= 1

    def is_two_pair(self, cards):
        return list(Counter(self.get_values(cards)).values()).count(2) >= 2

    def is_full_house(self, cards):
        counts = Counter(self.get_values(cards)).values()
        return 3 in counts and 2 in counts

    def is_straight_flush(self, cards):
        for suit in set(self.get_suits(cards)):
            suited = [c for c in cards if c.suit == suit]
            if len(suited) >= 5 and self.is_straight(suited):
                return True
        return False

    def is_royal_flush(self, cards):
        royal = {10, 11, 12, 13, 14}
        for suit in set(self.get_suits(cards)):
            suited = [c for c in cards if c.suit == suit]
            values = set(self.get_values(suited))
            if royal.issubset(values):
                return True
        return False

    # HAND EVALUATION
    def evaluate_hand(self, cards):

        values = self.get_values(cards)
        counts = Counter(values)
        sorted_vals = sorted(values, reverse=True)

        if self.is_royal_flush(cards):
            return (10, [14])

        if self.is_straight_flush(cards):
            return (9, sorted_vals[:5])

        if self.is_four_kind(cards):
            quad = max([v for v, c in counts.items() if c == 4])
            kicker = max([v for v in values if v != quad])
            return (8, [quad, kicker])

        if self.is_full_house(cards):
            triple = max([v for v, c in counts.items() if c == 3])
            pair = max([v for v, c in counts.items() if c == 2])
            return (7, [triple, pair])

        if self.is_flush(cards):
            return (6, sorted_vals[:5])

        if self.is_straight(cards):
            return (5, sorted_vals[:5])

        if self.is_three_kind(cards):
            triple = max([v for v, c in counts.items() if c == 3])
            kickers = sorted([v for v in values if v != triple], reverse=True)[:2]
            return (4, [triple] + kickers)

        if self.is_two_pair(cards):
            pairs = sorted([v for v, c in counts.items() if c == 2], reverse=True)
            kicker = max([v for v in values if v not in pairs])
            return (3, pairs + [kicker])

        if self.is_pair(cards):
            pair = max([v for v, c in counts.items() if c == 2])
            kickers = sorted([v for v in values if v != pair], reverse=True)[:3]
            return (2, [pair] + kickers)

        return (1, sorted_vals[:5])

    # WINNER
    def check_winner(self):

        human_cards = self.human.cards + self.community_cards
        computer_cards = self.computer.cards + self.community_cards

        human_score, human_kickers = self.evaluate_hand(human_cards)
        computer_score, computer_kickers = self.evaluate_hand(computer_cards)

        print("\n--- HAND RANKINGS ---")
        print(f"Human: {human_score} | {human_kickers}")
        print(f"Computer: {computer_score} | {computer_kickers}")

        if human_score > computer_score:
            return "human"
        if computer_score > human_score:
            return "computer"

        if human_kickers > computer_kickers:
            return "human"
        if computer_kickers > human_kickers:
            return "computer"

        return "tie"