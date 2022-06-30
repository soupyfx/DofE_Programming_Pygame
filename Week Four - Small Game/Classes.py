import pygame

class Settings():
    def __init__(self):
        self.upKEY = "w"
        self.downKEY = "s"

class Player(pygame.sprite.Sprite):
    def __init__(self,texture):
        super().__init__()
        self.image = pygame.image.load(texture)
        self.rect = self.image.get_rect()
        self.rect.center = [1400,500]
        self.health = 1
    def updatePlayerMovement(self,y):
        if y == -10:
            if self.rect.center[1] == 0:
                self.rect.move_ip(0,10)
        else:
            if self.rect.center[1] == 1000:
                self.rect.move_ip(0,-10)
        self.rect.move_ip(0,y)

class Obstacle(pygame.sprite.Sprite):
    def __init__(self,x,seed,uid):
        super().__init__()
        if seed >= 14:
            self.movementSpeed = 8
            self.image = pygame.image.load("Assets/Week Four/planetBig.png")
        elif seed >= 10:
            self.movementSpeed = 16
            self.image = pygame.image.load("Assets/Week Four/planetSmall.png")
        else:
            self.movementSpeed = 24
            self.image = pygame.image.load("Assets/Week Four/asteroid.png")
        self.rect = self.image.get_rect()
        self.rect.center = [-200,x]
        self.seed = seed
        self.uid = uid
    def update(self,obstacleGroup,playerGroup):
        self.rect.move_ip(self.movementSpeed,0)
        if self.rect.center[0] >= 1900:
            self.kill()
        if pygame.sprite.spritecollideany(self,obstacleGroup):
            if pygame.sprite.spritecollideany(self,obstacleGroup).seed > self.seed:
                self.kill()
            elif pygame.sprite.spritecollideany(self,obstacleGroup).seed == self.seed:
                if pygame.sprite.spritecollideany(self,obstacleGroup).uid != self.uid:
                    self.kill()


