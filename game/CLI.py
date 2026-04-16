from Game import Game


def get_highest_card(cards):
    rank_value = {
        "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
        "7": 7, "8": 8, "9": 9, "10": 10,
        "Jack": 11, "Queen": 12, "King": 13, "Ace": 14
    }

    best = 0

    for card in cards:
        value = rank_value.get(card.rank, 0)
        if value > best:
            best = value

    return best


def betting_round(human, computer, title):
    k = 0
    human_acted = False
    computer_acted = False

    while True:
        k += 1
        print(f"\n--- {title} ROUND {k} ---")

        action = human.choose_action()
        human_acted = True

        if action == "fold":
            print("Computer wins")
            return "computer"

        if action == "call":
            human.call(computer.total_bet_amount)

        if action == "raise":
            human.raise_bet(computer.total_bet_amount)

        comp = computer.auto_call_raise(human, k)
        computer_acted = True

        if comp == "fold":
            print("Human wins")
            return "human"

        if human_acted and computer_acted and human.total_bet_amount == computer.total_bet_amount:
            print("Betting matched. Moving on.")
            break

    return "continue"


def play_game():

    game = Game()

    human = game.human
    computer = game.computer

    game.turn = human

    # PRE-FLOP
    human_amount = human.place_initial_bet()
    computer_result = computer.auto_call_raise(human, 1)

    if computer_result == "fold":
        print("Computer folds. You win!")
        return

    game.pot = human.total_bet_amount + computer.total_bet_amount
    print("\nPOT:", game.pot)

    # FLOP
    game.deal_flop()
    game.show_community_cards()

    result = betting_round(human, computer, "POST FLOP")
    if result != "continue":
        return

    game.pot += human.total_bet_amount + computer.total_bet_amount
    human.reset()
    computer.reset()

    # TURN
    game.deal_turn()
    game.show_community_cards()

    result = betting_round(human, computer, "TURN")
    if result != "continue":
        return

    game.pot += human.total_bet_amount + computer.total_bet_amount
    human.reset()
    computer.reset()

    # RIVER
    game.deal_river()
    game.show_community_cards()

    result = betting_round(human, computer, "RIVER")
    if result != "continue":
        return

    game.pot += human.total_bet_amount + computer.total_bet_amount
    human.reset()
    computer.reset()

    # SHOWDOWN
    print("\n--- SHOWDOWN ---")
    print("Final Pot:", game.pot)

    human_cards = human.cards + game.community_cards
    computer_cards = computer.cards + game.community_cards

    human_score = get_highest_card(human_cards)
    computer_score = get_highest_card(computer_cards)

    print("\n--- HAND RESULT ---")
    print("Human best card value:", human_score)
    print("Computer best card value:", computer_score)

    if human_score > computer_score:
        print("You win the hand!")
    elif computer_score > human_score:
        print("Computer wins the hand!")
    else:
        print("It's a tie!")


play_game()