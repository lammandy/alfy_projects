import random

NUM_GAMES = 3


def play_game():
    p2 = input('Welcome to Rock, Paper, Scissors!\nTo face a human, type "human". To face a bot, type "bot". ')
    return p2

def rps_input(player):
    msg = 'Invalid!'
    while msg == 'Invalid!':
        choice = input(
            f'{player}, what will you play? For rock, type "r", for paper,'\
                 ' type "p", for scissor, type "s", followed by "enter". ')
        # if choice != 'r' or choice != 'p' or choice != 's':
        if choice == 'r' or choice == 'p' or choice == 's':
            msg = 'Valid!'
        elif choice == '!':
            return '!'
        else:
            msg = 'Invalid!'
        print(msg)
    return choice

def check_result(u1, u2):
    # draw = 0, p1 wins = 1, p2 wins = 2
    if u1 == u2:
        result = 'draws'
    elif (u1 == 'r' and u2 == 'p') or (u1 == 's' and u2 == 'r') or (u1 == 'p' and u2 == 's'):
        result = 'loses'
    else:
        result = 'wins'
    return result

def change_points(p1_score, p2_score, result):
    # checks results for player 1

    if result == 'loses':
        if p1_score > 0:
            p1_score -= 1
        p2_score += 1
    elif result == 'wins':
        p1_score += 1
        if p2_score > 0:
            p2_score -= 1
    return p1_score, p2_score

