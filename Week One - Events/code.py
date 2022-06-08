import pygame, sys

#A class for a small example of what you could use custom events
class Shop():
	def __init__(self):
		self.currentyOpen = True

shop = Shop()

#Vars
gameRunning = True

#Custom events / it starts at 24 because pygame uses the other ones
coolEvent = pygame.USEREVENT + 0 #24 + 0 / the id of the event is 24
coolEventE = pygame.event.Event(coolEvent, anythingIWant = "NiCe") # This creates event object with attributes IT CAN BE ANYTHING I WANT
closeShop = pygame.USEREVENT + 1 #24 + 1 / the id of the event is 25

#Stuff to initialize pygame (aka boring stuff lol)
pygame.init()
clock = pygame.time.Clock()
display = pygame.display.set_mode((1000,1000))

# This will trigger the close shop event after 1000ms
# The loops=1 means that it will loop once 0 for forever (0 it the default)
pygame.time.set_timer(closeShop, 1000, loops=1)

#Game loop
while gameRunning:
	#Gets all the events in a list 
	for event in pygame.event.get():
		#Just so i can close it
		if event.type == pygame.QUIT:
			pygame.QUIT()
			sys.exit()

		#A example of a built in event
		if event.type == pygame.MOUSEMOTION:
			print("Mouse is moving at ", event.pos)
		elif event.type == pygame.KEYDOWN:
			# This checks if you are pressing the lshift or rshift or both and c
			# USE THE bitwise operator & for checking mod in events!
			if event.key == pygame.K_c and event.mod & pygame.KMOD_SHIFT:
				pygame.event.post(coolEventE)

		#Custom Events
		if event.type == coolEvent: # Or the event id so 24
			print("It was cool")
			print(event.anythingIWant)
		elif event.type	== closeShop: # When close shop is triggered it will close the shop!
			shop.currentyOpen == False
			print("The shop is now closed")

	# Tells pygame how long to wait until the next frame in ms so 60ms
	clock.tick(60)
