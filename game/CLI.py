from Game import Game


def betting_round(human, computer, title):

    k = 0

    while True:
        k += 1
        print(f"\n--- {title} ROUND {k} ---")

        action = human.choose_action()

        if action == "fold":
            print("Human folds. Computer wins")
            return "computer"

        if action == "call":
            result = human.call(computer.total_bet_amount)
            if result == "fold":
                print("Human cannot call. Computer wins")
                return "computer"

        if action == "raise":
            result = human.raise_bet(computer.total_bet_amount)
            if result == "fold":
                print("Human cannot raise. Computer wins")
                return "computer"

        comp = computer.auto_call_raise(human, k)

        if comp == "fold":
            print("Computer folds. Human wins")
            return "human"

        if human.total_bet_amount == computer.total_bet_amount:
            print("Betting matched. Moving on.")
            break

    return "continue"


def play_game():

    game = Game()

    human = game.human
    computer = game.computer

    print("\n--- GAME START ---\n")

    print("Computer cards:")
    for c in computer.cards:
        print(c)

    print("\nHuman cards:")
    for c in human.cards:
        print(c)

    # PRE-FLOP
    human.place_initial_bet()
    comp = computer.auto_call_raise(human, 1)

    if comp == "fold":
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

    # TURN
    game.deal_turn()
    game.show_community_cards()

    result = betting_round(human, computer, "TURN")
    if result != "continue":
        return

    # RIVER
    game.deal_river()
    game.show_community_cards()

    result = betting_round(human, computer, "RIVER")
    if result != "continue":
        return

    # SHOWDOWN
    print("\n--- SHOWDOWN ---")
    print("Final Pot:", game.pot)

    winner = game.check_winner()

    if winner == "human":
        print("You win the hand!")
    elif winner == "computer":
        print("Computer wins the hand!")
    else:
        print("It's a tie!")


play_game()