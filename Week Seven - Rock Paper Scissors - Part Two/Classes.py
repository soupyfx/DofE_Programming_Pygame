import pygame

class Game():
	def __init__(self,maxLives):
		self.computerLives = maxLives
		self.playerLives = maxLives
		self.currentLevel = 0
	def takeLives(self,player):
		if player == "player":
			self.playerLives -= 1
		elif player == "computer":
			self.computerLives -= 1
		else:
			print("Please supply a proper argument")
		self.currentLevel += 1
        
  


