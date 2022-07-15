import pygame   #First is to import pygame module and open display window
from pygame.locals import *   #allows ommission of pygame.locals call before value pull 

pygame.init()   #initialise the pygame module and allow acccess to its functions
game_display = pygame.display.set_mode((800, 600))  #Sets display ration to 800 by 600
pygame.display.set_caption('My First Game')     #Sets top bar as game name
game_display.fill('white') #Sets display fill as white

def event_handler():    #define the event handler actions
    for event in pygame.event.get():    #'get' function on current event.type value
        if (event.type == QUIT):    
            pygame.quit()       #if the 'get' returns 'QUIT' as value, exit
while True:
    event_handler()     
    pygame.display.update()     #while the above is true, update the display


