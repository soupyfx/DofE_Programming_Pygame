import pygame, sys
import random as rand
from Classes import *

#Vars
gameRunning = True
gameOver = False
moveUp = False
moveDown = False
settings = Settings()
score = 0

#Initialize the player sprite
player = Player("Assets/Week Four/player.png")
playerGroup = pygame.sprite.Group()
playerGroup.add(player)

#Initialize the obstacle group
obstacleGroup = pygame.sprite.Group()

#Custom Events
summonEnemy = pygame.USEREVENT + 0

#Stuff to initialize pygame (aka boring stuff lol)
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
display = pygame.display.set_mode((1700,1000))

pygame.time.set_timer(summonEnemy, 200)

font = pygame.font.SysFont('freesansbold.ttf', 50)



#Game loop
while gameRunning:
	#Handling Events#
	#Summoning the obstacles
	if pygame.event.get(summonEnemy):
		if gameOver:
			continue
		else:
			obstacle = Obstacle(rand.randrange(10,990),rand.randrange(0,15),rand.randrange(1,10000000000))
			obstacleGroup.add(obstacle)
	#For deteting all other events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameRunning = False
		#To detect key clicking
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.key.key_code(settings.downKEY):
				moveDown = True
			if event.key == pygame.key.key_code(settings.upKEY):
				moveUp = True
			if event.key == pygame.key.key_code("r"):
				if gameOver:
					gameOver = False
					player.health = 10
					score = 0
		elif event.type == pygame.KEYUP:
			if event.key == pygame.key.key_code(settings.downKEY):
				moveDown = False
			if event.key == pygame.key.key_code(settings.upKEY):
				moveUp = False


	#To move the player when there is a input
	if moveDown == True:
		player.updatePlayerMovement(10)
	if moveUp == True:
		player.updatePlayerMovement(-10)

	if pygame.sprite.spritecollide(player,obstacleGroup,True):
		player.health -= 1

	if player.health <= 0:
		gameOver = True
		pygame.event.clear()
	else:
		score += 1

	healthText = "Health: "+str(player.health)
	scoreText = "Score: "+str(score)
	healthTX = font.render(healthText, True, (255,255,255))
	scoreTX = font.render(scoreText, True, (255,255,255))
	restartTX = font.render("Press R to Restart", True, (255,255,255))

	#Drawing stuff to the display
	pygame.display.flip() 
	display.fill((0,0,0))
	playerGroup.draw(display)
	obstacleGroup.draw(display)
	obstacleGroup.update(obstacleGroup,playerGroup)
	if gameOver:
		display.blit(restartTX, (750,480))
		display.blit(scoreTX, (750, 520))
	else:
		display.blit(healthTX, (20, 20))
		display.blit(scoreTX, (220, 20))
	clock.tick(60)

pygame.quit()
sys.exit()