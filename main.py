import random

print("H A N G M A N  # 8 attempts")

words = ["python", "java", "swift", "javascript"]
win_games = 0
lost_games = 0
user_menu = ""


def guess_letters():
    answer = random.choice(words)
    guessed_letters_set = set()
    all_letters_set = set()
    attempt = 8
    global win_games, lost_games
    while attempt > 0:
        if all(w in guessed_letters_set for w in answer):
            break
        print()
        [print(w, end="") if w in guessed_letters_set else print("-", end="") for w in answer]
        print()

        user_input = input("Input a letter: ")

        if len(user_input) != 1:
            print("Please, input a single letter")
            continue
        if not user_input.isalpha():
            print("Please, enter a lowercase letter from the English alphabet.")
            continue

        if not user_input.islower():
            print("Please, enter a lowercase letter from the English alphabet.")
            continue

        if user_input in all_letters_set:
            print("You've already guessed this letter.")
            continue

        if user_input not in answer:
            all_letters_set.add(user_input)
            attempt -= 1
            print("That letter doesn't appear in the word.  # {} attempts".format(attempt))
            continue

        if user_input in answer and user_input not in guessed_letters_set:
            guessed_letters_set.add(user_input)
            all_letters_set.add(user_input)
            continue

    if all(w in guessed_letters_set for w in answer):
        win_games += 1
        print("You guessed the word {}!".format(answer))
        print("You survived!")
    else:
        lost_games += 1
        print("\nYou lost!")


def menu(user_input):
    menu_set = ("play", "results", "exit")
    while user_input not in menu_set:
        user_input = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    if user_input == "play":
        guess_letters()
    if user_input == "results":
        print("You won: {} times".format(win_games))
        print("You lost: {} times".format(lost_games))
    if user_input == "exit":
        exit()


while user_menu != "exit":
    menu(user_menu)
