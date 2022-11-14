from hangman_helper import *

words = load_words()
wrong_guess_lst = []
points = POINTS_INITIAL
on = True
games = 0
def update_word_pattern(word, pattern, letter):
    in_word = False
    for i in range(len(word)):
        if word[i] == letter:
            pattern[i] = letter
            in_word = True
    if not in_word:
        wrong_guess_lst.append(letter)
    return pattern

def run_single_game(words, points):
    word = get_random_word(words)
    pattern = []
    for i in range(len(word)):
        pattern.append('_')
    msg = 'Welcome to Hangman!'
    while '_' in pattern and points > 0:
        display_state(pattern, wrong_guess_lst, points, msg)
        choice = get_input()
        if choice[0] == 1:
            letter = choice[1]
            if not letter.isalpha():
                msg = 'Incorrect input.'
            elif letter in wrong_guess_lst or letter in pattern:
                msg = 'Letter already guessed.'
            else:
                update_word_pattern(word, pattern, letter)
                if choice[1] in word:
                    n = word.count(choice[1])
                    points += n*(n+1)//2
                    msg = 'Letter in word!'
                else:
                    msg = 'Letter not in word.'
                points -= 1
        elif choice[0] == 2:
            points -= 1
            if word == choice[1]:
                n = pattern.count('_')
                points = n*(n+1)//2
                msg = 'You are the winner!'
                pattern = word
            else:
                msg = 'Wrong word.'
        else:
            points -= 1
            i_letters = []
            hinted_words = []

            print(f"indx letters before: {i_letters}")
            print(hinted_words)
            for i in range(len(word)):
                if pattern[i] != '_':
                    i_letters.append(i)
            for i in i_letters:
                word[i]

            for w in words:
                if len(hinted_words) == HINT_LENGTH:
                    break
                count = 0
                if len(w) == len(word):
                    for i in i_letters:
                        if w[i] == word[i]:
                            count += 1
                        else:
                            break
                    if count == len(i_letters):
                        hinted_words.append(w)
            msg = hinted_words
            print(f"indx letters after: {i_letters}")
    if play_again(msg):
        return points
while points:
    points = run_single_game(words,points)
    games += 1
    print(f'You have played {games} game(s)!')