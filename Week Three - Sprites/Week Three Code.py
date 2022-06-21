import pygame, sys
import random as rand

class Person(pygame.sprite.Sprite):
	#Constructor to initialize the object 
	def __init__(self,image,x,y):
		super().__init__() #Calls the parent constructor (Sprite)
		#Grabs a image for the sprite with the image
		self.image = pygame.image.load(image)
		#Creates a rect around it (For detecting collisions)
		self.rect = self.image.get_rect()
		#Moves the rect center point to x,y (Witch is randomly genrated)
		self.rect.center = [x,y]

# This is just for detecing collisions with the sprite and mouse
class Mouse(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		#Creates a image for the sprite
		self.image = pygame.Surface((1,1))
		self.image.fill((255,255,255,0))
		#Creates a rect around it (For detecting collisions)
		self.rect = self.image.get_rect()
	def update(self):#Updates pos to the pos of the mouse
		self.rect.center = pygame.mouse.get_pos()
	def click(self):#If the player clicks
		if pygame.sprite.spritecollide(mouse,friendlyGroup,True):
			print("You lose")
		elif pygame.sprite.spritecollide(mouse,enemyGroup,True):
			print("You win")
		else:
			print("You missed")

#Vars
gameRunning = True

#Stuff to initialize pygame (aka boring stuff lol)
pygame.init()
clock = pygame.time.Clock()
display = pygame.display.set_mode((1000,1000))

#Create a enemy from my class
enemy = Person("Assets/Week Three/enemy.png",rand.randrange(20,980),rand.randrange(20,980))
#We need to create a group because you cant render sprites indvidually you need to group before you can render
#Create a group called enemyGroup
enemyGroup = pygame.sprite.Group()
#Adds it to group enemyGroup
enemyGroup.add(enemy)

#Does the same as the enemy group but makes many of them
friendlyGroup = pygame.sprite.Group()
for i in range(25):# Makes 25 friendly sprites
	#Creates the friendly and selects a random pos
	friendly = Person("Assets/Week Three/friendly.png",rand.randrange(20,980),rand.randrange(20,980))
	#Adds it to group friendlyGroup
	friendlyGroup.add(friendly)

#Does the same but for a diffrent sprite class
mouse = Mouse()
mouseGroup = pygame.sprite.Group()
mouseGroup.add(mouse)


#Game loop
while gameRunning:
	#Just so I can close it
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameRunning = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			mouse.click()

	#Updates the screen so that its viewed in the window
	pygame.display.flip() 
	#Tells pygame to draw the group (ORDER MATTERS AGAIN)
	display.fill((255,255,255))
	friendlyGroup.draw(display)
	enemyGroup.draw(display)
	mouseGroup.draw(display)
	mouseGroup.update()
	# Tells pygame how long to wait until the next frame in ms so 60ms
	clock.tick(60)

pygame.quit()
sys.exit()