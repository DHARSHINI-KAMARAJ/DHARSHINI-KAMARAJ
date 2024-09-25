import random


word_list = ["python", "C", "C++", "programming", "computer", "science"]

def choose_word():
    return random.choice(word_list)

def display_hangman(attempts):
    
    stages = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        =========
        """,
    ]
    return stages[attempts]

def play_game():
    word = choose_word()
    word_display = ["_"] * len(word)
    guessed_letters = set()
    attempts = 6

    print("Welcome to Hangman!")
    print(display_hangman(attempts))
    print("Word: " + " ".join(word_display))

    while attempts > 0 and "_" in word_display:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try again.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            for index, letter in enumerate(word):
                if letter == guess:
                    word_display[index] = letter
            print(f"Good guess: {guess}")
        else:
            attempts -= 1
            print(f"Wrong guess: {guess}. Attempts remaining: {attempts}")

        print(display_hangman(attempts))
        print("Word: " + " ".join(word_display))

    if "_" not in word_display:
        print("Congratulations! You guessed the word:", word)
    else:
        print("Sorry, you've run out of attempts. The word was:", word)

if __name__ == "__main__":
    play_game()
