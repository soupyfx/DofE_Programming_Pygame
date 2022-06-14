import pygame, sys

#Vars
gameRunning = True

rectY = 0
rectX = 0

#Colors 
#(r,g,b)
red = pygame.Color(255,0,0)
green = pygame.Color(0,255,0)
blue = pygame.Color(0,0,255)
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)

# Creates a Rect (Not to be confused with rect)
# This allows me to transform/move ecta the rectange
# I will go more in depth into this in a later date
rectange = pygame.Rect((400,400), (200,200))

#Stuff to initialize pygame (aka boring stuff lol)
pygame.init()
clock = pygame.time.Clock()
display = pygame.display.set_mode((1000,1000))

#Creates a surface
screen = pygame.Surface((1000,1000))

#Game loop
while gameRunning:
	#Just so I can close it
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameRunning = False # A better way of doing it
		if event.type == pygame.MOUSEMOTION:
			mousePos = event.pos

	# REMEBER ORDER MATTERS THINGS THAT ARE FIRST WILL END UP UNDER OTHER THINGS

	#Fills the screen with the color black (just a example)
	screen.fill(white)

	#Drawing Shapes the first and second requirements are the same The Screen, Color
	#Here are some examples of what you can do
	pygame.draw.rect(screen, (0,255,255,255), rectange)
	pygame.draw.rect(screen, blue, [0, 0, 100, 100])
	pygame.draw.line(screen, red, (0,0), mousePos)
	pygame.draw.aaline(screen, green, (1000,0),mousePos, True)
	pygame.draw.polygon(screen, black, [[300, 100], [0, 200], mousePos], 3)

	#Updates the screen so that its viewed in the window
	display.blit(screen, (0,0))
	pygame.display.flip()
	# Tells pygame how long to wait until the next frame in ms so 60ms
	clock.tick(60)

pygame.quit()
sys.exit()
