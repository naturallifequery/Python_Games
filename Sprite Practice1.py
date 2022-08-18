#Pygame new project template
import pygame
import random

WIDTH = 360  # width of our game window
HEIGHT = 480 # height of our game window
FPS = 30 # frames per second

# Colors (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

     
    def update(self):
        self.rect.x += 5
        if self.rect.left > WIDTH:
            self.rect.right = 0



pygame.init()
pygame.mixer.init()  # for sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("NEWGAME")
clock = pygame.time.Clock()

#Sprite groups (for faster sprite draw and animation load times)
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Game Loop
running = True
while running:
    #keep loop running at correct speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
    # check for closing window
        if event.type == pygame.QUIT:
            running = False


    # Update - what do the sprites need to do, animations etc
    all_sprites.update()


    # Draw / render - draw sprite /backgrounds on screen
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
