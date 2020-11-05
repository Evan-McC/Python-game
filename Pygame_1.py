import pygame
import random
import os

WIDTH = 400
HEIGHT = 400
FPS = 30

#Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#Asset
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

#Player Class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "Character.png")).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.y_speed = 5

    def update(self):
        #Return List of Keys pressed
        keystate = pygame.key.get_pressed()

        #Keys to press
        if keystate[pygame.K_RIGHT]:
            self.rect.x += 5
        if keystate[pygame.K_LEFT]:
            self.rect.x += -5
        if keystate[pygame.K_UP]:
            self.rect.y += -5
        if keystate[pygame.K_DOWN]:
            self.rect.y += 5
        

#Platform Class
class Platform(pygame.sprite.Sprite):
    def __init__(self):
        self.rect.x = 400
        self.rect.y = -375

    def update(self):
        self.rect.x += -5
        

        #Variables
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Pygame")

clock = pygame.time.Clock()

#Sprite Groups
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

#Game Loop:
    #Process Events
    # Update
    #Draw

running = True
while running:

    clock.tick(FPS)

    #Process Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Update
    all_sprites.update()
    
    #Draw
    screen.fill (BLACK)
    all_sprites.draw(screen)
    
    #Flip
    pygame.display.flip()

pygame.quit()
