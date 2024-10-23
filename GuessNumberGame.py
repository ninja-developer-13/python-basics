import random
lowerBound = 1
upperBound = 100
maxAttempts = 10
class GuessNumberGame:
    def __init__(self):
        self.randomNumber = random.randint(lowerBound, upperBound)
    def guessNumber(self):
        #print("system generated number",self.randomNumber)
        for attempt in range(maxAttempts):
            guess = int(input(f"Guess the number between {lowerBound} and {upperBound}: "))
            if guess > self.randomNumber:
                print(f"Sorry {guess} is too high!")
            elif guess < self.randomNumber:
                print(f"Sorry {guess} is too low!")
            else:
                print(f"{guess} is correct!")
                break
obj = GuessNumberGame()
obj.guessNumber()

