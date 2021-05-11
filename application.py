Class Phrase: words = 3 spaces = 2 letters = 11

def__init__(self, phrase) self.is_compliment = True self.phrase = phrase self.phrase = phrase.upper() self.missed = 0 #should this ‘missed’ have a variable before it or stay here or go under def make _guess? self.phrase = [Phrase(‘YOU ARE GREAT!’)] self.active_phrase = self.get_random.phrase

def make_guess(self): while True: if self.missed == 5 print(“You can only guess wrong 5 times. Sorry the game now ends.”) else: print(“Good job! You guessed them all correctly..”)

def go(self, guess): #does this not look right? while True try: guess = input (‘Guess a letter’) if self.guess(): if self.is_wrong print (‘Guess again’) self.is_wrong = False print(‘You guessed right’) else: print(‘You ran out of guesses’) self.stop

def open(self, guess): for letter in self.phrase: if guess in self.phrase: return True else: return False
