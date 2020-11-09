import pygame
import random
import os

#Constants
WIDTH = 400
HEIGHT = 400
FPS = 30
GROUND = HEIGHT - 30
SLOW = 3
FAST = 10

#Constant Physics
PLAYER_ACC = 0.9
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.9
vec = pygame.math.Vector2

#Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#Asset
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

#Applying friction on x-axis


#Player Class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "Character.png")).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

        self.pos = vec(10, GROUND - 60)
        self.vel = vec(0,0)
        self.acc = vec(0,0)

    def update(self):

        self.acc = vec(0, PLAYER_GRAV)
        
        #Return List of Keys pressed
        keystate = pygame.key.get_pressed()
        
        if keystate[pygame.K_RIGHT]:
            self.acc.x += PLAYER_ACC
        if keystate[pygame.K_LEFT]:
            self.acc.x += -PLAYER_ACC
        if self.vel.y == 0 and keystate[pygame.K_SPACE]:
            self.vel.y = -20

        #Apply friction in the x direction
        self.acc.x += self.vel.x * PLAYER_FRICTION

        #Equations of Motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        #Wrap arpund the screen
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        #Simulate the Ground
        if self.pos.y > GROUND:
            self.pos.y = GROUND + 1
            self.vel.y = 0

        #Set the new player position based on above
        self.rect.midbottom = self.pos

#Platform Class
class Platform(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface ((100, 25))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = HEIGHT - 80

    def update(self):
        self.rect.x += -3
        if self.rect.right < 0:
            self.rect.left = WIDTH
        
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

platform = Platform()
all_sprites.add(platform)

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
