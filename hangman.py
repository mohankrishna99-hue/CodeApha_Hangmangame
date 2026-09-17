import random

def play_hangman():
    # Small list of 5 predefined words
    words = ["python", "guitar", "puzzle", "planet", "forest"]
    
    # Pick a random word from the list
    secret_word = random.choice(words)
    
    # Lists and variables to track game state
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect = 6

    print("=" * 40)
    print("------ WELCOME TO HANGMAN GAME! ------       ")
    print("=" * 40)
    print(f"Guess the secret word! It has {len(secret_word)} letters.")
    print(f"You are allowed a maximum of {max_incorrect} incorrect guesses.\n")

    # Main game loop
    while incorrect_guesses < max_incorrect:
        # Construct the displayed word with revealed letters and underscores
        display_word = []
        for letter in secret_word:
            if letter in guessed_letters:
                display_word.append(letter)
            else:
                display_word.append("_")

        # Check if player won
        if "_" not in display_word:
            print("\n" + "*" * 40)
            print(f" Congratulations! You won!")
            print(f" The secret word was: {secret_word.upper()}")
            print("*" * 40)
            break

        # Display current game status
        print("Word to guess: " + " ".join(display_word))
        print(f"Guessed letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")
        print(f"Incorrect guesses remaining: {max_incorrect - incorrect_guesses}")

        # Prompt player for a guess
        guess = input("Enter a letter: ").strip().lower()

        # Validate input using if-else
        if len(guess) != 1 or not guess.isalpha():
            print("--> Please enter a single valid alphabet letter.\n")
            continue

        if guess in guessed_letters:
            print(f"--> You already guessed '{guess}'. Try another letter.\n")
            continue

        # Add the guess to the list of guessed letters
        guessed_letters.append(guess)

        # Evaluate the guess
        if guess in secret_word:
            print(f"--> Nice! '{guess}' is in the word.\n")
        else:
            incorrect_guesses += 1
            print(f"--> Oops! '{guess}' is not in the word.\n")

    # Loss condition
    if incorrect_guesses >= max_incorrect:
        print("=" * 40)
        print(" GAME OVER! You ran out of guesses.")
        print(f"The secret word was: {secret_word.upper()}")
        print("=" * 40)

if __name__ == "__main__":
    play_hangman()

