import random

# 1. List of predefined words
with open("word.txt", "r") as file:
    words = file.read().splitlines()


# 2. Hangman drawings
hangman_stages = [
    """
    +---------+
    |         |
    |         |
    |         |
    |         |
    |         |
    +---------+
    """,

    """
    +---------+
    |         |
    |       ( )
    |         |
    |         |
    |         |
    +---------+
    """,

    """
    +---------+
    |         |
    |       ( )
    |        |
    |        |
    |         |
    +---------+
    """,

    """
    +---------+
    |         |
    |       ( )
    |       /|
    |        |
    |         |
    +---------+
    """,

    """
    +---------+
    |         |
    |       ( )
    |       /|\\
    |        |
    |         |
    +---------+
    """,

    """
    +---------+
    |         |
    |       ( )
    |       /|\\
    |       / |
    |         |
    +---------+
    """,

    """
    +---------+
    |         |
    |       (X)
    |       /|\\
    |       / \\
    |         |
    +---------+
    """
]


def play_game():

    # 3. Select a random word
    word = random.choice(words)

    # 4. Create blanks for the word
    guessed_word = ["_"] * len(word)

    # 5. Store guessed letters
    guessed_letters = []

    # 6. Store incorrect guesses
    wrong_letters = []

    # 7. Maximum incorrect guesses
    max_attempts = 6
    attempts = 0

    print("\n" + "-" * 40)
    print("        WELCOME TO HANGMAN")
    print("-" * 40)

    print(f"\nThe word has {len(word)} letters.")
    print("You have 6 incorrect guesses available.")

    # 8. Main game loop
    while attempts < max_attempts and "_" in guessed_word:

        print(hangman_stages[attempts])

        print("Word:", " ".join(guessed_word))
        print("Wrong letters:", " ".join(wrong_letters))
        print("Attempts remaining:", max_attempts - attempts)

        # 9. Take input
        guess = input("\nGuess a letter: ").lower().strip()

        # 10. Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only ONE alphabetic letter.")
            continue

        # 11. Check repeated guess
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        # Add guess to guessed letters
        guessed_letters.append(guess)

        # 12. Check whether letter is in word
        if guess in word:

            print("Correct guess!")

            # Reveal all positions containing the letter
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess

        else:

            print("Wrong guess!")
            wrong_letters.append(guess)
            attempts += 1

    # 13. Game result
    print(hangman_stages[attempts])

    if "_" not in guessed_word:
        print("Word:", " ".join(guessed_word))
        print("\n🎉 Congratulations! You won!")
        print("You guessed the word:", word)

    else:
        print("\n💀 Game Over!")
        print("The correct word was:", word)


# 14. Play again feature
while True:

    play_game()

    choice = input("\nDo you want to play again? (yes/no): ").lower().strip()

    if choice != "yes":
        print("\nThanks for playing Hangman!")
        break