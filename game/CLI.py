from Game import Game

def play_game():

    game = Game()

    human = game.human
    computer = game.computer

    game.turn = human

    # HUMAN BET
    human_amount = human.place_initial_bet()
    human.update_amount_bet(human_amount)

    # COMPUTER RESPONSE
    computer_amount = computer.auto_match_or_raise(human_amount)
    computer.update_amount_bet(computer_amount)

    # CHECK FOLD
    if computer_amount == "l":
        print("Computer folds. You win!")
        return

    # POT
    game.pot = human_amount + computer_amount

    print("\n--- ROUND RESULT ---")
    print("Human bet:", human_amount)
    print("Computer bet:", computer_amount)
    print("Pot:", game.pot)


play_game()