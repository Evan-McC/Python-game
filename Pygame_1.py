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
'''
PLAYER_ACC = 0.9
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.9
vec = pygame.math.Vector2
'''

#Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#Asset
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")
snd_folder = os.path.join(game_folder, "snd")

#Draw Text
font_name = pygame.font.match_font("arial")
def draw_text (surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, RED)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    screen.blit (text_surface, text_rect)

#Show start screen function
def show_start_screen():
    screen.fill(WHITE)
    draw_text(screen, "Game_Title", 64, WIDTH / 2, HEIGHT / 4)
    draw_text(screen, "Move around with the Mouse", 22, WIDTH / 2, HEIGHT / 2)    
    draw_text(screen, "Press any key to begin...", 18, WIDTH /2, HEIGHT *3 / 4)
    pygame.display.flip()
    print(start)
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    print("Game Start")
                    waiting = False


#Game Over Screen
def show_GameOver_screen():
    screen.fill(BLACK)
    draw_text(screen, "GAME OVER", 100, WIDTH / 2, HEIGHT / 2)
    pygame.display.flip()
    StartOver = True
    while StartOver:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_TAB:
                    StartOver = False
                    start = True
                    print(start)


#Player Class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "Character.png")).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

        '''
        self.pos = vec(10, GROUND - 60)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        '''
        
    def update(self):
        
        #Return List of Keys pressed
        keystate = pygame.key.get_pressed()
        
        if keystate[pygame.K_d]:
            self.rect.x += 10
        if keystate[pygame.K_a]:
            self.rect.x += -10
        if keystate[pygame.K_w]:
            self.rect.y += -10
        if keystate[pygame.K_s]:
            self.rect.y += 10

        '''
        #Apply friction in the x direction
        self.acc.x += self.vel.x * PLAYER_FRICTION

        #Equations of Motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        '''

        '''
        #Wrap arpund the screen
        if self.rect.left > WIDTH:
            self.rect.right = 0
        if self.rect.right < 0:
            self.rect.left = WIDTH

        if self.rect.bottom > HEIGHT:
            self.rect.top = 0
        if self.rect.top < 0:
            self.rect.bottom = HEIGHT
        '''
        
        '''
        #Simulate the Ground
        if self.pos.y > GROUND:
            self.pos.y = GROUND + 1w
            self.vel.y = 0
        
        #Set the new player position based on above
        self.rect.midbottom = self.pos
        '''
        
        '''
        #Hit Platform
        hits = pygame.sprite.spritecollide(self, floors, False)
        if hits:
            if self.rect.top > hits[0].rect.top: #Jumping from underneath
                self.rect.y = hits[0].rect.bottom + 25 + 1
                
            else:
                self.rect.bottom = hits[0].rect.top - 1 #Jumping from above
        '''
        #Keep player on screen
                #Right
        if self.rect.right > WIDTH - 5:
            self.rect.right = WIDTH - 5
                #Left
        if self.rect.left < 5:
            self.rect.left = 5
                #Bottom
        if self.rect.bottom > HEIGHT - 5:
            self.rect.bottom = HEIGHT - 5
                #Top
        if self.rect.top < 5:
            self.rect.top = 5
"""
        #Lose condition if player touches hand
        contact = pygame.sprite.spritecollide(hand, False)
        if contact:
"""           
            
        
                
#Hand Class
class Hand(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "Hand.png")).convert()
        self.rect = self.image.get_rect()
    def update (self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
'''       
#Floor Class
class Floor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface ((WIDTH, 10))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = HEIGHT - 10

#Wall Right Class
class Wall_R(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface ((10, HEIGHT))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH - 10
        self.rect.y = 0      
'''
        
#Variables
    #Start Game
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame_1")

clock = pygame.time.Clock()


#Load Sounds


#Sprite Groups
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

hand = Hand()
all_sprites.add(hand)
'''
floor = Floor()
all_sprites.add(floor)
wall_r = Wall_R()
all_sprites.add(wall_r)

floors = pygame.sprite.Group()
floors.add(floor)
floors.add(wall_r)
'''
#Game Loop:
    #Process Events
    # Update
    #Draw

start = True
GAMEOVER = False
running = True
while running:

    #Show start screen once
    if start:
        show_start_screen()
        start = False

    clock.tick(FPS)

    #Game Over Screen
    if GAMEOVER:
        show_GameOver_screen()
        GAMEOVER = False
            

    #Process Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_F2:
                print("Game over")
                GAMEOVER = True

    #Update
    all_sprites.update()
    
    #Draw
    screen.fill (BLACK)
    all_sprites.draw(screen)
    
    #Flip
    pygame.display.flip()

pygame.quit()
