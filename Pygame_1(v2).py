import pygame
import random
import os

#Constants
WIDTH = 800
HEIGHT = 500
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

#Draw Text
font_name = pygame.font.match_font("arial")
def draw_text (screen, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    screen.blit (text_surface, text_rect)

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
            self.vel.y = -12

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

#Floor Class
class Floor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface ((WIDTH, 25))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH
        self.rect.y = HEIGHT - 475

#Platform Class
class Platform(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface ((100, 25))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH / 2
        self.rect.y = HEIGHT - 80

    def update(self):
        self.rect.x += 0
        if self.rect.right < 0:
            self.rect.left = WIDTH

#Platform Class 2
class Platform_2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface ((25, 100))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH - 700
        self.rect.y = HEIGHT - 250

    def update(self):
        self.rect.y += 3
        if self.rect.bottom < HEIGHT:
            self.rect.top = 0

#Platform Class 3
class Platform_3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface ((100, 25))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH - 200
        self.rect.y = HEIGHT - 500

    def update(self):
        self.rect.y += 3
        if self.rect.bottom < HEIGHT:
            self.rect.top = 0
        
#Variables
    #Start Game
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Pygame")

clock = pygame.time.Clock()

#Sprite Groups
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

floor = Floor()
all_sprites.add(floor)

platform = Platform()
all_sprites.add(platform)

platform_2 = Platform_2()
all_sprites.add(platform_2)

platform_3 = Platform_3()
all_sprites.add(platform_3)

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
