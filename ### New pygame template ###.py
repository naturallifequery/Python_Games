#-------------  New Pygame Template -------------#
import pygame as pg
import turtle as ttl
import random 


#-------------  Game Settings -------------#
### Window Settings ###
WIDTH = 600
HEIGHT = 480
FPS = 60

### RGB Setup ###
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
PURPLE = (255,0,255)
CYAN = (0,255,255)

#-------------  Define Classes -------------#
class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()





### initialise pygame and create window ###
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("GAME_TEMPLATE")
clock = pg.time.Clock()

### Sprite groups (for faster sprite draw and animation load times) ###

#~ All Sprites Group ~#
all_sprites = pg.sprite.Group()

player = Player()
all_sprites.add(player)




#-------------  Game Loop -------------#
running = True
while running:
#keep loop running at correct speed
    clock.tick(FPS)
    # Process input (events)
    for event in pg.event.get():
    # check for closing window
        if event.type == pg.QUIT:
            running = False

    ### Process input (events) ###

    
    ### Update ###
all_sprites.update()

    ### Draw / Render ###
screen.fill(BLACK)
all_sprites.draw(screen)
#~ *after* drawing everything, flip the display ~#
pg.display.flip()

pg.quit()