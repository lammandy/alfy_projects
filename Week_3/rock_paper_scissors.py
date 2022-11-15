import random

from rock_paper_scissors_helper import rps_input
from rock_paper_scissors_helper import check_result
from rock_paper_scissors_helper import change_points
from rock_paper_scissors_helper import NUM_GAMES
from rock_paper_scissors_helper import play_game

def man_vs_man_game(p2):
    p1_score = 0
    p2_score = 0
    on = True
    while p1_score < 3 and p2_score < 3 and on:
        p1_choice = rps_input('Player 1')
        if p2 == 'human':
            p2_choice = rps_input('Player 2')
            if p2_choice == '!':
                break
        if p1_choice == '!':
            break
        elif p2 == 'bot':
            p2_choice = random.choice(['r', 'p', 's'])
            print(f'Bot plays {p2_choice}')
        result = check_result(p1_choice, p2_choice)

        if result == 'draws':
            print('Draw!')
        else:
            print(f'Player 1 {result}')
        p1_score, p2_score = change_points(p1_score, p2_score, result)
        print(f'Player 1: {p1_score}\nPlayer 2: {p2_score}')
while True:
    p2 = play_game()
    man_vs_man_game(p2)
    play = input('Play again? "y" for yes, "n" for no. ')
    play = play.lower()
    if play == 'n':
        break


