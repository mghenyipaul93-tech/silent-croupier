import random
import time


class Player:

    def __init__(self, type="computer", cards=None, total_bet_amount=0, name="", balance=1000):
        self.type = type
        self.cards = cards if cards is not None else []
        self.total_bet_amount = total_bet_amount
        self.name = name
        self.balance = balance

    # HUMAN BETTING
    
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

    
    # COMPUTER BETTING
   
    def auto_match_or_raise(self, current_bet):

        print("Computer is thinking...")
        time.sleep(1.5)

        action = random.choice(["match", "raise"])

        # MATCH LOGIC
        if action == "match":
            if self.balance >= current_bet:
                self.balance -= current_bet
                self.total_bet_amount += current_bet
                print(f"Computer matched the bet: {current_bet}")
                return current_bet
            else:
                print("Computer cannot match. Folds.")
                return 0

        # RAISE LOGIC
        raise_amount = random.randint(1, max(1, self.balance // 2))
        total_needed = current_bet + raise_amount

        if total_needed > self.balance:
            total_needed = self.balance

        self.balance -= total_needed
        self.total_bet_amount += total_needed

        print(f"Computer raised by {raise_amount} (total bet: {total_needed})")
        return total_needed

    # BET UPDATE 
   
    def update_amount_bet(self, amount):
        self.total_bet_amount += amount

    # RESET FOR NEW ROUND

    def reset(self):
        self.cards = []
        self.total_bet_amount = 0