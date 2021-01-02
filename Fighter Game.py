import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0,0,255)

maps = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

#Initialise Pygame
pygame.init()
 
#Classes
class Player(pygame.sprite.Sprite):
         def __init__(self):
             super().__init__()
             self.health = 100
             self.xp = 0
             self.score = 0
             self.kills = 0
             self.level = 0
        
             #Set player image and location
             self.image = pygame.image.load("PlayerGuy.png").convert()
             self.image.set_colorkey(BLACK)
             self.rect=self.image.get_rect()
             self.rect.x=100
             self.rect.y=100
        
         def move(self,x,y):
             self.x_speed += x
             self.y_speed += y
        
         def update(self, wall):

            #Moves the player
            self.rect.x += self.x_speed
            self.rect.y =+ self.y_speed
            
            #Checks for collisions between player and wall
            player_hit_list = pygame.sprite.spritecollide(player, wall, False) 

            for player in player_hit_list:

                #If the player is moving right, set the right edge of the player, to the left edge of the wall (stops it going through) and vice versa if moving left
                if player.x_speed > 0:
                    player.rect.right = wall.rect.left
                elif player.x_speed < 0: 
                    player.rect.left = wall.rect.right
                
                #Same as above, if the player hits the top wall, set the bottom edge of the 
                elif player.y_speed > 0:
                    player.rect.bottom = wall.rect.top
                elif player.y_speed < 0:
                    player.rect.top = wall.rect.bottom

                    


            

class Wall(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()

        #Makes a wall with size 40x40
        self.image = pygame.surface.Surface([40,40])
        self.image.fill(BLUE)

        #Make the wall where we pass in the x and y paramaters
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y






#Pygame lists for collisions 

all_sprites_list = pygame.sprite.Group()

player_list = pygame.sprite.Group()
player_hit_list = pygame.sprite.Group()

wall_list = pygame.sprite.Group()
wall_hit_list = pygame.sprite.Group()

bullet_list = pygame.sprite.Group()
bullet_hit_list = pygame.sprite.Group()




# Set the width and height of the screen [width, height]
size = (800, 800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Fighter Game")



#Create instance of player and add it to relevant lists 
player = Player()
player_list.add(player)
all_sprites_list.add(player)

#Creating temporary walls to test whether the collisions so far work
for y in range(20):
    for x in range(20):
        if maps[y][x] == 1:
            wall=Wall(x*40, y*40)
            all_sprites_list.add(wall)
            wall_list.add(wall)




# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
  
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
    all_sprites_list.update
    
 
    # --- Drawing code should go here
    all_sprites_list.draw(screen)
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
