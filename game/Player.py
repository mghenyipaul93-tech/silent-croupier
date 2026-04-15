import random
import time


class Player:

    def __init__(self, type="computer", cards=None, total_bet_amount=0, name="", balance=1000):
        self.type = type
        self.cards = cards if cards is not None else []
        self.total_bet_amount = total_bet_amount
        self.name = name
        self.balance = balance

    def place_initial_bet(self):
        while True:
            amount = input(f"{self.name}, balance {self.balance}, enter bet: ")

            if amount.isdigit() and 0 < int(amount) <= self.balance:
                amount = int(amount)
                self.balance -= amount
                self.total_bet_amount += amount
                return amount
            else:
                print("Invalid input.")

    def choose_action(self):
        choice = input("1: Call | 2: Fold | 3: Raise: ")

        if choice == "1":
            return "call"
        elif choice == "2":
            return "fold"
        elif choice == "3":
            return "raise"
        else:
            print("Invalid choice")
            return self.choose_action()

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

    def fold(self):
        print(f"{self.name} folds.")
        return "fold"

    def raise_bet(self, opponent_bet):
        while True:
            amount = input(f"Enter raise amount (balance {self.balance}): ")

            if amount.isdigit() and int(amount) > 0:
                amount = int(amount)
                total = (opponent_bet - self.total_bet_amount) + amount

                if total <= self.balance:
                    self.balance -= total
                    self.total_bet_amount += total
                    print(f"{self.name} raises by {amount}")
                    return total
                else:
                    print("Not enough balance.")
            else:
                print("Invalid input.")

    def auto_action(self, opponent_bet):
        print("Computer is thinking...")
        time.sleep(1.5)

        diff = opponent_bet - self.total_bet_amount

        if diff > self.balance:
            print("Computer folds.")
            return "fold"

        action = random.choice(["call", "raise"])

        if action == "call":
            return self.call(opponent_bet)

        raise_amount = random.randint(1, max(1, self.balance // 3))
        total = diff + raise_amount

        if total > self.balance:
            total = self.balance

        self.balance -= total
        self.total_bet_amount += total

        print(f"Computer raises by {raise_amount}")
        return total

    def reset(self):
        self.cards = []
        self.total_bet_amount = 0