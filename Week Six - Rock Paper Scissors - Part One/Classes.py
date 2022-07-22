import pygame

class Button(pygame.sprite.Sprite):
	def __init__(self,x,y,image,action,display):
		super().__init__()
		self.display = display
		self.action = action
		self.image = pygame.image.load(image).convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.center = [x,y]
		self.pressed = False
	def update(self):
		mousePos = pygame.mouse.get_pos()
		if self.rect.collidepoint(mousePos):
			if pygame.mouse.get_pressed()[0] == 1 and not self.pressed:
				action = self.action
				self.pressed = True
				print("Based Raito")
			elif pygame.mouse.get_pressed()[0] == 0:
				self.pressed = False

		self.display.blit(self.image, (self.rect.x, self.rect.y))

