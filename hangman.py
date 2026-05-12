import random
from os import system

HANGMAN_STAGES = [
r"""
 _________
|        |
|        |
|        
|
|
|
|
|__________
""",
r"""
 _________
|        |
|        |
|        O
|
|
|
|
|__________
""",
r"""
 _________
|        |
|        |
|        O
|        |
|        |
|
|
|__________
""",
r"""
 _________
|        |
|        |
|        O
|       \|
|        |
|
|
|___________
""",
r"""
 _________
|        |
|        |
|        O
|       \|/
|        |
|
|
|___________
""",
r"""
 _________
|        |
|        |
|        O
|       \|/
|        |
|       /
|
|___________
""",
r"""
 _________
|        |
|        |
|        O
|       \|/
|        |
|       / \
|
|___________
"""
]

# opens the file and reads each of the lines in it, removing any whitespace, then choosing a random word in the words list.
def get_random_word():
    # need to change the location of the words list used here.
    with open("C:/Users/justw/Desktop/wordList.txt", "r") as f:
        words = [word.strip() for word in f.readlines() if word.strip().isalpha() and len(word.strip()) >= 5]
    return random.choice(words).lower()


# replace the letters with '_ '
def set_guessing_word(word: str):
    return " ".join("_" for _ in word)


# set the guessed letter at each occurence.
def update_guessing_word(pos, guessing_word, letter):
    word = list(guessing_word)
    for i in pos:
        # this is necessary because of the spaces in guessing_word.
        word[i + i] = letter
    return word


# if the letter is in the word, return the position(s) that the letter occurs in the word.
def get_positions(letter: str, word: str):
    return [pos for pos in range(len(word)) if word[pos] == letter]


# initializes everything for the game, and runs a loop while the user hasn't won/lost. 
# it updates the UI to reflect how the user is doing, and shows messages based on how the user performs.
def game_loop():
    word = get_random_word()
    wrong_letters = []
    correct_count: int = 0
    errors_remaining: int = 6
    guessing_word = set_guessing_word(word)

    while errors_remaining > 0:
        system('cls')
        print(HANGMAN_STAGES[6 - errors_remaining])
        print("\n" + guessing_word)
        print(f"Wrong letters: {' '.join(wrong_letters)}")
        while True:
            try:
                letter = input("Enter a letter: ").strip().lower()
                if not letter.isalpha() or letter in wrong_letters or letter in guessing_word or len(letter) > 1:
                    raise ValueError()
                break
            except ValueError:
                print("You must enter a valid and unused letter!")               
        if letter in word:
            positions = get_positions(letter, word)
            guessing_word = ''.join(update_guessing_word(
                positions, guessing_word, letter))
            print(guessing_word)
            correct_count += len(positions)
            if correct_count == len(word):
                system('cls')
                print("YOU WON!")
                print(HANGMAN_STAGES[6 - errors_remaining])
                print("\n" + guessing_word)
                break
        else:
            wrong_letters.append(letter)
            errors_remaining -= 1
            if (errors_remaining == 0):
                system('cls')
                print('YOU LOST!')
                print(HANGMAN_STAGES[6 - errors_remaining])
                print(f"The word was {word}")
                break


# calls the game loop to play, and handles main input
def main():
    while True:
        try:
            choice = int(input("Enter a choice:\n1) Play\n2) Quit\nInput: "))
            if choice not in [1, 2]:
                raise ValueError()
            if choice == 1:
                game_loop()
            else:
                exit()
        except ValueError:
            print("You must enter either 1 or 2!")


if __name__ == "__main__":
    main()
