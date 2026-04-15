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
            amount = input(
                f"{self.name}, current balance is {self.balance}, enter your bet: "
            )

            if amount.isdigit() and 0 < int(amount) <= self.balance:
                amount = int(amount)
                self.total_bet_amount += amount
                self.balance -= amount
                return amount
            else:
                print("Invalid input. Enter a number within your balance.")

  
   
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

  
    def call(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.total_bet_amount += amount
            print(f"{self.name} calls {amount}")
            return amount
        else:
            print(f"{self.name} cannot call. Not enough balance.")
            return 0

    def fold(self):
        print(f"{self.name} folds.")
        return "fold"

    def raise_bet(self, current_bet):
        while True:
            amount = input(f"Enter raise amount (balance: {self.balance}): ")

            if amount.isdigit() and int(amount) > 0:
                amount = int(amount)
                total = current_bet + amount

                if total <= self.balance:
                    self.balance -= total
                    self.total_bet_amount += total
                    print(f"{self.name} raises by {amount}")
                    return total
                else:
                    print("Not enough balance.")
            else:
                print("Invalid input.")

    
   
    def auto_match_or_raise(self, current_bet):

        print("Computer is thinking...")
        time.sleep(1.5)

        action = random.choice(["match", "raise"])

        # MATCH
        if action == "match":
            if self.balance >= current_bet:
                self.balance -= current_bet
                self.total_bet_amount += current_bet
                print(f"Computer matched the bet: {current_bet}")
                return current_bet
            else:
                print("Computer folds.")
                return 0

        # RAISE
        raise_amount = random.randint(1, max(1, self.balance // 2))
        total_needed = current_bet + raise_amount

        if total_needed > self.balance:
            total_needed = self.balance

        self.balance -= total_needed
        self.total_bet_amount += total_needed

        print(f"Computer raised by {raise_amount} (total bet: {total_needed})")
        return total_needed

   
    def update_amount_bet(self, amount):
        self.total_bet_amount += amount

   
    def reset(self):
        self.cards = []
        self.total_bet_amount = 0