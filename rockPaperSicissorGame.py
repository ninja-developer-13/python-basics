import random
class RockPaperSicissorGame:
    choices = ["Rock", "Paper", "Scissor"]
    def __init__(self, userChoice):
        self.userChoice = userChoice.capitalize()
    def play(self):
        computerChoice = random.choice(self.choices)
        print(computerChoice)
        if self.userChoice == computerChoice:
            print("It's a tie!")
        elif (self.userChoice == "Rock" and computerChoice == "Scissor") or \
                (self.userChoice == "Paper" and computerChoice == "Rock") or \
                (self.userChoice == "Scissor" and computerChoice == "Paper"):
            print("You win!")
        else:
            print("You lose!")


userInput = str(input("Please enter choice fron (Rock,Paper,Scissor): "))
obj = RockPaperSicissorGame(userInput)
obj.play()