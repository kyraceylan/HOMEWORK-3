class rockpaperscissor:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def play(self):
        if self.player1 == self.player2:
            return "It's a tie!"
        elif (self.player1 == "rock" and self.player2 == "scissor") or
                (self.player1 == "scissor" and self.player2 == "paper") or
                (self.player1 == "paper" and self.player2 == "rock"):
            return "Player 1 wins!"
        else:            return "Player 2 wins!"
# Example usage:
game = rockpaperscissor("rock", "scissor")
result = game.play()
print(result)  # Output: Player 1 wins!
game = rockpaperscissor("paper", "rock")
result = game.play()
print(result)  # Output: Player 1 wins!
game = rockpaperscissor("scissor", "paper")
result = game.play()
print(result)  # Output: Player 1 wins!
game = rockpaperscissor("rock", "paper")
result = game.play()
print(result)  # Output: Player 2 wins!
game = rockpaperscissor("scissor", "rock")
result = game.play()
print(result)  # Output: Player 2 wins!
game = rockpaperscissor("paper", "scissor")
result = game.play()
print(result)  # Output: Player 2 wins!
game = rockpaperscissor("rock", "rock")
result = game.play()
print(result)  # Output: It's a tie!
game = rockpaperscissor("paper", "paper")
result = game.play()
print(result)  # Output: It's a tie!
game = rockpaperscissor("scissor", "scissor")
result = game.play()
print(result)  # Output: It's a tie!
