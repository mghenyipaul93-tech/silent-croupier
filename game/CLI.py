from Game import Game


def play_game():

    game = Game()

    human = game.human
    computer = game.computer

    game.turn = human

    human_amount = human.place_initial_bet()

    computer_result = computer.auto_action(human.total_bet_amount)

    if computer_result == "fold":
        print("Computer folds. You win!")
        return

    game.pot = human_amount + (computer_result if computer_result else 0)

    print("\n--- ROUND RESULT ---")
    print("Human bet:", human_amount)
    print("Computer action completed")
    print("Pot:", game.pot)

    k = 0

    print("\n--- BETTING ROUND ---")

    while True:

        k += 1

        if human.total_bet_amount == computer.total_bet_amount:
            print("Bets matched. Round ends.")
            break

        print(f"\n--- TURN {k} ---")

        human_choice = human.choose_action()

        if human_choice == "fold":
            print("Computer wins")
            return

        if human_choice == "call":
            human.call(computer.total_bet_amount)

        if human_choice == "raise":
            human.raise_bet(computer.total_bet_amount)

        computer_choice = computer.auto_action(human.total_bet_amount)

        if computer_choice == "fold":
            print("Human wins")
            return

        print("STATUS")
        print("Human bet:", human.total_bet_amount)
        print("Computer bet:", computer.total_bet_amount)

    game.pot = human.total_bet_amount + computer.total_bet_amount

    print("\n--- ROUND END ---")
    print("Final Pot:", game.pot)


play_game()