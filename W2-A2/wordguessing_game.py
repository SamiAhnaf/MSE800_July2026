import random
import string


class WordGuessingGame:
    def __init__(self, max_lives=6):

        self.max_lives = max_lives # Store the maximum number of lives for the game.

        
        self.words = [
            "python", "variable", "function", "iterator", "notebook",
            "pipeline", "dataset", "computer", "research", "analytics"
        ] # Store the list of possible words.

        # These variables will be set when a new game starts.
        self.secret = ""
        self.blanks = []
        self.lives = max_lives
        self.used_letters = set()

    def get_random_word(self):
        
        return random.choice(self.words) # Randomly select one word from the word list.

    def make_blanks(self, word):

        return ["_" for _ in word] # Create one blank "_" for every letter in the word.

    def prompt_for_letter(self):

        while True: # Keep asking until the user enters a valid, unused letter.
            guess = input("Guess a letter: ").strip().lower()

            if len(guess) != 1 or guess not in string.ascii_lowercase: # Check that the user entered exactly one A-Z letter.
                print("→ Please enter a single A-Z letter.")
                continue

            if guess in self.used_letters: # Check whether the letter has already been used.
                print("→ You already tried that letter.")
                continue

            return guess

    def reveal_letters(self, letter): # Check the secret word and reveal matching letters.

        found_any = False

        for i, ch in enumerate(self.secret):
            if ch == letter and self.blanks[i] == "_":
                self.blanks[i] = letter
                found_any = True

        return found_any

    def all_blanks_filled(self): 
        return "_" not in self.blanks  # Return True when there are no "_" characters left.

    def play(self): # Start a new game by selecting a word and creating blanks.
        self.secret = self.get_random_word()
        self.blanks = self.make_blanks(self.secret)
        self.lives = self.max_lives
        self.used_letters = set()

        print("\nWelcome to Word Guessing!")
        print(f"The word has {len(self.secret)} letters.")
        print(" ".join(self.blanks))

        while True:
            guess = self.prompt_for_letter() # Ask the user to guess a letter.
            self.used_letters.add(guess)

            if self.reveal_letters(guess): # Check whether the guessed letter is in the word.
                print("\nWell done, Nice job! You found a letter.")
                print(" ".join(self.blanks))

                if self.all_blanks_filled(): # Check whether the player has guessed the whole word.
                    print("\nCongratulations! You guessed the word!")
                    print(f"Word: {self.secret}")
                    print("GAME OVER")
                    break

            else:
                self.lives -= 1  # The guessed letter was incorrect, so remove one life.
                print(f"\nNope. You lose a life. Lives left: {self.lives}")
                print(" ".join(self.blanks))

                if self.lives <= 0: # Check whether the player has run out of lives.
                    print("\nOut of lives! Sad story!")
                    print(f"The word was: {self.secret}")
                    print("GAME OVER")
                    break


def main(): # Create a WordGuessingGame object with 6 lives.
    game = WordGuessingGame()

    # Start the game.
    game.play()


if __name__ == "__main__":
    main()