import pygame, sys
from Classes import *
from Functions import *

gameRunning = True
action = ""
playerChoice = ""
cpuChoice = ""

pygame.init()
clock = pygame.time.Clock()
display = pygame.display.set_mode((960,540))

font = pygame.font.SysFont('freesansbold.ttf', 50)

buttonGroup = pygame.sprite.Group()
button = Button(100,100,"Assets/Week Six/temp.png","E",display)
buttonGroup.add(button)

createText("hello",font,(255,255,255),50,50,display)

while gameRunning:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameRunning = False

	pygame.display.flip() 
	buttonGroup.update()
	clock.tick(60)

pygame.QUIT()
sys.exit()