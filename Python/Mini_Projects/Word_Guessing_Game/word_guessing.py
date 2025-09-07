# Word Guessing Game
# A simple game where the player has to guess a secret word letter by letter.

import random  # Import the random module to pick a word randomly

# Step 1: Create a list of possible secret words
word_bank = ['rizz', 'ohio', 'sigma', 'tiktok', 'skibdi']

# Step 2: Randomly choose one word from the list
word = random.choice(word_bank)

# Step 3: Create a hidden version of the word with underscores
# Example: If word is 'rizz', then word_guess = ['_', '_', '_', '_']
word_guess = ['_'] * len(word)

# Step 4: Set number of attempts (like lives)
attempt = 6

# Step 5: Run the game loop until the player runs out of attempts
while attempt > 0:
    # Display the current guessed word with spaces
    print('\nCurrent Word: ' + ' '.join(word_guess))

    # Ask the player to guess a letter and convert it to lowercase
    guess = input('Guess a letter: ').lower()

    # Step 6: If the guess is in the word
    if guess in word:
        # Loop through the word to reveal all matching positions
        for i in range(len(word)):
            if word[i] == guess:
                word_guess[i] = guess
        print('Great guess!')  # Positive feedback
    else:
        # Wrong guess: lose one attempt
        attempt -= 1
        print('Wrong guess! Attempts left: ' + str(attempt))

    # Step 7: Check if the player has guessed the entire word
    if '_' not in word_guess:
        print('\nCongratulations!! You guessed the word: ' + word)
        break  # Exit the loop

# Step 8: If player used all attempts and still didn’t guess
if attempt == 0 and '_' in word_guess:
    print('\nYou have run out of attempts! The word was: ' + word)