import pygame, sys
from Classes import *
from Functions import *

gameRunning = True
inGame = False
currentMenu = "mainMenu"

pygame.init()
clock = pygame.time.Clock()
display = pygame.display.set_mode((960,540))

font = pygame.font.SysFont('freesansbold.ttf', 50)

while gameRunning:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameRunning = False
		if event.type == pygame.KEYDOWN:
			if inGame:
				inGame = False
				currentMenu = "endMenu"
				continue # In the game menu
			else:
				if event.key == pygame.key.key_code("h"):
					currentMenu = "helpMenu"
				if event.key == pygame.key.key_code("n"):
					game = Game(3)
					currentMenu = "gameMenu"
					inGame = True
				if event.key == pygame.key.key_code("x"):
					currentMenu = "mainMenu"

   
	if inGame:
		drawMenu(currentMenu,game.playerLives,game.computerLives,game.currentLevel,display,font)
	else:
		drawMenu(currentMenu,1,1,1,display,font)

	pygame.display.flip() 
	clock.tick(60)

pygame.QUIT()
sys.exit()
