from game_logic import GameLogic
  
if __name__ == '__main__':
  game = GameLogic()
  game.start()


File 2: game_logic.py

import random
from string import ascii_letters
from phrase import Phrase 

class GameLogic:

  def __init__(self):
    self.missed = 0
    self.phrases = [
        Phrase("simplicity becomes elegance"), 
        Phrase("i do not fear computers"),
        Phrase("programming is fun"),
        Phrase("imagination is more important than knowledge"),
    ]
    self.active_phrase = self.random_phrase()

    #this is the list that holds the letters that user has guessed
    self.guesses = [" "]

  def random_phrase(self):
    # choose a phrase from the list above
    return random.choice(self.phrases)

 def start(self):
    print("Print welcome message")
    while self.missed != 5 and not self.active_phrase.check_complete(self.guesses):
            # Print missed guesses counter
        print(f"{' '*11}Wrong guesses: {self.missed}\n")
        self.active_phrase.display(self.guesses)
            # call the get_guess method and assign it to a variable
        user_guess = self.get_guess()
           # Add the user's guess to guesses list
        self.guesses.append(user_guess)
            # Increment the number of missed attempts by 1
        if not self.active_phrase.check_letters(user_guess):
                print("Bummer!")
                self.missed += 1
        else:
            # if the guess is incorrect, calls the game_over method
            self.game_over()

 def get_guess(self):
    while True:
      try:
        guess_input = input("\n\n Guess a letter:> ").lower()
        if len(guess_input) != 1 or not guess_input.isalpha():
           raise ValueError("Try again using only lowercase alphabets")
      except ValueError as err:
          print(f"Invalid input {err}")
          continue
      else:
         return guess_input

  def game_over(self):
        if self.active_phrase.check_complete(self.guesses):
            print(" Congratulations\n   **You won**")
            #self.replay()
        elif self.missed == 5:
            print("\n\n    Game Over!\nBetter luck next time.")
            #self.replay()


File 3: phrase.py

class Phrase:
    def __init__(self, phrase):
      # makes everything lower case so it is easier to compare   
      self.phrase = phrase.lower()

    # this will either print the letters that are guessed correctly or
    # show a blank line where they should be
    def display(self, guesses):
        #for each letter in the phrase
        for letter in self.phrase:
            # if letter is in the guesses list, show it to user
            if letter in guesses:
                print(f"{letter}", end=" ")
            else:
                # else print the placeholder
                print("_", end=" ")

    def check_letters(self, guesses):
        return guesses in self.phrase

    def check_complete(self, guesses):
        for letter in self.phrase:
            if letter not in guesses:
                return False
        return True


