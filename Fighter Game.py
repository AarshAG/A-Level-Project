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



class Player(pygame.sprite.Sprite):
         def __init__(self,x,y):
             super().__init__()
             self.health = 100
             self.xp = 0
             self.score = 0
             self.kills = 0
             self.level = 0
             self.x_speed = 0
             self.y_speed = 0

             #Set player image and location
             self.image = pygame.image.load("PlayerGuy.png").convert()
             self.image.set_colorkey(BLACK)
             self.rect=self.image.get_rect()
             self.rect.x=100
             self.rect.y=100

         def move(self,x,y):

             #Adds the movement values to the x and y of player
             self.x_speed += x
             self.y_speed += y

         def update(self):

            #Moves the player on x-axis
            self.rect.x += self.x_speed

            #Check if player collides with an object in wall_list, if it does, add to player_hit_list.
            player_hit_list = pygame.sprite.spritecollide(player, wall_list, False)

            for wall in player_hit_list:
                if player.x_speed > 0:                  #if the player is moving right and it hits a wall
                    player.rect.right = wall.rect.left  #Set right edge of player to left edge of wall to stop it going through
                elif player.x_speed < 0:                #Same as above, but the opposite (moving left)
                    player.rect.left = wall.rect.right

            #Moves player on y-axis
            self.rect.y += self.y_speed

            #Check if player collides with an object in wall_list, if it does, add to
            # player_hit_list.
            player_hit_list = pygame.sprite.spritecollide(player, wall_list, False)


            for wall in player_hit_list:
                if player.y_speed > 0: #if player is moving down and hits a wall,
                    player.rect.bottom = wall.rect.top #set bottom of player to top of wall
                elif player.y_speed < 0: # Same as above but opposite (moving up)
                    player.rect.top = wall.rect.bottom

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([15, 15])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        x_speed = 0
        y_speed = 0
        self.rect.x = player.rect.x         #Make the bullet spawn where the player is at
        self.rect.y = player.rect.y

        pos = pygame.mouse.get_pos()        #Get mouse position
        mouse_x = pos[0]                    #Get x coordinate of mouse position
        mouse_y = pos[1]                    #Get y coordinate of mouse position
        rise = mouse_x - player.rect.x      #Work out the width difference between player and mouse
        run = mouse_y - player.rect.y       #Work out the height difference between player and mouse
        self.x_speed = rise/50              #Set the movement vectors as the difference between player and mouse so bullet goes to mouse
        self.y_speed = run/50               #Divide by 10 to slow down the bullet (goes too fast otherwise)



    def update(self):

        self.rect.x += self.x_speed         #Add the speeds onto the coordinates of the bullet
        self.rect.y += self.y_speed







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
player = Player(200,200)
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
        elif event.type == pygame.KEYDOWN:     #Making the player move.
            if event.key == pygame.K_LEFT:     #If you want to go left, you -3 from the x coordinate.
                player.move(-3,0)
            elif event.key == pygame.K_RIGHT:
                player.move(3,0)
            elif event.key == pygame.K_UP:     #If you want to go up, you -3 from the y coordinate
                player.move(0,-3)
            elif event.key == pygame.K_DOWN:
                player.move(0,3)
            elif event.key == pygame.K_SPACE:
                bullet = Bullet()
                bullet_list.add(bullet)
                all_sprites_list.add(bullet)

        elif event.type == pygame.KEYUP:      #Making the player stop
            if event.key == pygame.K_LEFT:    #Since you want the player to stop, you have to do the opposite
                player.move(3,0)              #action as above so that 0 gets added to the x or y
            elif event.key == pygame.K_RIGHT:
                player.move(-3,0)
            elif event.key == pygame.K_UP:
                player.move(0,3)
            elif event.key == pygame.K_DOWN:
                player.move(0,-3)

    # --- Game logic should go here
    all_sprites_list.update()

    while len(bullet_list) > 3:             #Makes it so that only 3 bullets can be on the screen at a time
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)

            
    for bullet in bullet_list:              #Remove bullet if it collides with wall
        if pygame.sprite.spritecollide(bullet, wall_list, False):
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)




    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)

    # --- Drawing code should go here
    all_sprites_list.draw(screen)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
