import random
import time


class Player:

    def __init__(self, type="computer", cards=None, total_bet_amount=0, name="", balance=1000):
        self.type = type
        self.cards = cards if cards is not None else []
        self.total_bet_amount = total_bet_amount
        self.name = name
        self.balance = balance

    def reset(self):
        self.cards = []
        self.total_bet_amount = 0

    # INITIAL BET
    def place_initial_bet(self):
        while True:
            amount = input(f"{self.name}, balance {self.balance}, enter bet: ")

            if amount.isdigit():
                amount = int(amount)

                if 0 < amount <= self.balance:
                    self.balance -= amount
                    self.total_bet_amount += amount
                    return amount

            print("Invalid input or insufficient balance.")

    # ACTION
    def choose_action(self):
        choice = input("1: Call | 2: Fold | 3: Raise: ")

        if choice == "1":
            return "call"
        if choice == "2":
            return "fold"
        if choice == "3":
            return "raise"

        print("Invalid choice")
        return self.choose_action()

    # CALL
    def call(self, opponent_bet):
        diff = opponent_bet - self.total_bet_amount

        if diff <= 0:
            print(f"{self.name} checks.")
            return 0

        if diff > self.balance:
            print(f"{self.name} cannot call.")
            return "fold"

        self.balance -= diff
        self.total_bet_amount += diff

        print(f"{self.name} calls {diff}")
        return diff

    # FOLD
    def fold(self):
        print(f"{self.name} folds.")
        return "fold"

    # RAISE
    def raise_bet(self, opponent_bet):

        if self.balance <= 0:
            print(f"{self.name} has no balance.")
            return "fold"

        while True:
            amount = input(f"Enter raise amount (balance {self.balance}): ")

            if not amount.isdigit():
                print("Invalid input.")
                continue

            amount = int(amount)

            if amount <= 0:
                print("Raise must be greater than 0.")
                continue

            diff = opponent_bet - self.total_bet_amount
            total_required = diff + amount

            if total_required > self.balance:
                print("Not enough balance for this raise.")
                return "fold"

            self.balance -= total_required
            self.total_bet_amount += total_required

            print(f"{self.name} raises by {amount}")
            return total_required

    # COMPUTER AI
    def auto_call_raise(self, opponent, round_count):

        print("Computer is thinking...")
        time.sleep(1.0)

        opponent_bet = opponent.total_bet_amount
        diff = opponent_bet - self.total_bet_amount

        print(f"Human bet: {opponent_bet}")
        print(f"Computer bet: {self.total_bet_amount}")

        if diff <= 0:
            print("Computer checks.")
            return 0

        if diff > self.balance:
            print("Computer cannot match and folds.")
            return "fold"

        action = random.choice(["call", "raise"])

        if round_count >= 3:
            action = "call"

        if action == "call":
            self.balance -= diff
            self.total_bet_amount += diff
            print(f"Computer calls {diff}")
            return diff

        max_raise = max(1, self.balance - diff)
        raise_amount = random.randint(1, min(50, max_raise))

        total = diff + raise_amount

        self.balance -= total
        self.total_bet_amount += total

        print(f"Computer raises by {raise_amount}")
        return total