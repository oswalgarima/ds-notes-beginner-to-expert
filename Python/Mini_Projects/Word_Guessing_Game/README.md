⸻

# Word Guessing Game in Python

A fun terminal-based game to guess a hidden word letter by letter. Designed using beginner Python logic and conditionals. Great for learning loops, strings, and lists.

---

## Problem:

**Guess the word correctly before you run out of chances!**  
**Word Bank:** `['rizz', 'ohio', 'sigma', 'tiktok', 'skibdi']`  
**Total Attempts:** `6`  
**Victory:** If all letters are guessed in time  
**Failure:** If all attempts are used up

---

## Python Code

```python
import random 
word_bank = ['rizz', 'ohio', 'sigma', 'tiktok', 'skibdi']

word = random.choice(word_bank)
word_guess = ['_'] * len(word)

attempt = 6

while attempt > 0:
    print('\nCurrent Word: ' + ' '.join(word_guess))

    guess = input('Guess a letter: ').lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                word_guess[i] = guess
        print('Great guess!')
    else:
        attempt -= 1
        print('Wrong guess! Attempts left: ' + str(attempt))

    if '_' not in word_guess:
        print('\n Congratulations!! You guessed the word: ' + word)
        break

if attempt == 0 and '_' in word_guess:
    print('\nYou have run out of attempts! The word was: ' + word)

```
⸻

## Beginner-Friendly Explanation Table

|  Concept 	           |  Child-Level Explanation                                   |
|----------------------|------------------------------------------------------------|
| `random.choice()`    | Pick one word randomly like drawing from a hat             |
| `['_'] * len()`      | Create blank spaces for each letter in the word            |
| `for i in range`     | Go through each letter’s position one by one               |
| `if guess in word`   | Check if your guess is in the secret word                  |
| `input()`            | Ask the player to guess a letter                           |
| `attempt -= 1`       | Decrease your chances if the guess is wrong                |
| `' '.join()`         | Nicely display the guessed letters with spaces             |

⸻

 One-Line Summary

“A letter-guessing game that teaches you loops, conditionals, and string manipulation—all in one!”

⸻

 Flash Revision Prompts
	1.	What Python function is used to randomly pick a word?
	2.	Why do we use ['_'] * len(word) at the beginning?
	3.	How does the game detect a correct letter?
	4.	What happens when all blanks are filled?

⸻

 Citation

 Inspired by: Practice project from beginner Python series

⸻

**Made with 💙 by [@oswalgarima](https://github.com/oswalgarima)**  
*Learning out loud, one note at a time 🚀*
