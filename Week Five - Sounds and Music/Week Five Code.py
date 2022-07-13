import pygame, sys, math

#Vars
gameRunning = True
gameVolume = 0.1

#Stuff to initialize pygame (aka boring stuff lol)
pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
display = pygame.display.set_mode((1000,1000))

# This loads the sound you need to do this for each sound you want to use
ding = pygame.mixer.Sound("Assets/Week Five/ding.mp3")
quack = pygame.mixer.Sound("Assets/Week Five/quack.mp3")

#This loads the game music only one file can be loaded in music at a time!
pygame.mixer.music.load("Assets/Week Five/MineDiamonds.mp3")
pygame.mixer.music.play(loops=-1)# This plays the currently loaded music the loops=-1 means that it loops 1 time
#pygame.mixer.music.unload() this unloads the music

pygame.mixer.music.queue("Assets/Week Five/shutdown.mp3") # This queus the song so it plays after the other one has ended
#This will never play because I set the loops to -1 meaning that the first song will play forever

#Inits a font so I can display volume on the screen
font = pygame.font.SysFont('freesansbold.ttf', 100)

#Game loop
while gameRunning:
	#Gets all the events in a list 
	for event in pygame.event.get():
		#Just so i can close it
		if event.type == pygame.QUIT:
			gameRunning = False
		#This allows me to input changes for the volume
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.key.key_code("w"):
				gameVolume += 0.01
				ding.play()#This plays the sound that is loaded in the var it goes varName.play()
			if event.key == pygame.key.key_code("s"):
				gameVolume -= 0.01
				quack.play()#This plays the sound that is loaded in the var it goes varName.play()

	print(pygame.mixer.music.get_pos()) # This prints the amount of time the music has been on in ms

	#Some valdation for the number that they inputed
	gameVolume = round(gameVolume, 3)
	if gameVolume < 0 or gameVolume > 1:
		 gameVolume = 0.5

	#This sets the volume of the music according to the selected volume
	pygame.mixer.music.set_volume(gameVolume)

	#Renders the volume so I can see it on the screen
	gameVolumeTX = font.render(str(gameVolume), True, (0,255,255))
	pygame.display.flip()
	display.fill((0,0,0))
	display.blit(gameVolumeTX, (20, 20))
	# Tells pygame how long to wait until the next frame in ms so 60ms
	clock.tick(60)

pygame.QUIT()
sys.exit()