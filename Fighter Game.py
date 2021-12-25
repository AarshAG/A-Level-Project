
#Import libraries
import pygame
import random
import math
from os import path
import time


# Define some colors
BLACK = (0, 0, 0)
GRAY = (105, 105, 105)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0,0,255)
ORANGE = (255,140,0)
LIGHTORANGE = (252, 160, 65)
WIDTH = 800
HEIGHT = 800




#Initialise Pygame
pygame.init()


# --------------------- Classes --------------------- #

class Wall(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()

        #Makes a wall with size 40x40
        self.image = pygame.image.load("WallImage.jpg").convert()
        self.rect=self.image.get_rect()

        #Make the wall where we pass in the x and y paramaters
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y



class Player(pygame.sprite.Sprite):
         def __init__(self):
             super().__init__()
             self.health = 1000
             self.score = 0
             self.kills = 0
             self.coins = 0
             self.damage = 5
             self.x_speed = 0
             self.y_speed = 0

             #Set player image and location

             self.sprite_images_right = [] #Create list of images

             self.sprite_images_right.append(pygame.image.load("PlayerRight1.png").convert()) #All the images are walking cycles 1 frame ahead of each other
             self.sprite_images_right.append(pygame.image.load("PlayerRight2.png").convert()) #Add all the images to a list
             self.sprite_images_right.append(pygame.image.load("PlayerRight3.png").convert()) #Since there are seperate animations for when the player is moving
             self.sprite_images_right.append(pygame.image.load("PlayerRight4.png").convert()) #left, and right, two different variables, and lists must be used
             self.sprite_images_right.append(pygame.image.load("PlayerRight5.png").convert())
             self.sprite_images_right.append(pygame.image.load("PlayerRight6.png").convert())
             self.sprite_images_right.append(pygame.image.load("PlayerRight7.png").convert())
             self.sprite_images_right.append(pygame.image.load("PlayerRight8.png").convert())
             self.sprite_images_right.append(pygame.image.load("PlayerRight9.png").convert())
             self.sprite_images_right.append(pygame.image.load("PlayerRight10.png").convert())
             self.sprite_images_right.append(pygame.image.load("PlayerRight11.png").convert())
             self.sprite_images_right.append(pygame.image.load("PlayerRight12.png").convert())

             self.current_image_right = 0 #Count variable used for when the player is walking right


             self.sprite_images_left = []   #Create list of images

             self.sprite_images_left.append(pygame.image.load("PlayerLeft1.png").convert()) #All the images are walking cycles 1 frame ahead of each other
             self.sprite_images_left.append(pygame.image.load("PlayerLeft2.png").convert()) #Add all the images to a list
             self.sprite_images_left.append(pygame.image.load("PlayerLeft3.png").convert()) #Since there are seperate animations for when the player is moving
             self.sprite_images_left.append(pygame.image.load("PlayerLeft4.png").convert()) #left, and right, two different variables, and lists must be used
             self.sprite_images_left.append(pygame.image.load("PlayerLeft5.png").convert())
             self.sprite_images_left.append(pygame.image.load("PlayerLeft6.png").convert())
             self.sprite_images_left.append(pygame.image.load("PlayerLeft7.png").convert())
             self.sprite_images_left.append(pygame.image.load("PlayerLeft8.png").convert())
             self.sprite_images_left.append(pygame.image.load("PlayerLeft9.png").convert())
             self.sprite_images_left.append(pygame.image.load("PlayerLeft10.png").convert())
             self.sprite_images_left.append(pygame.image.load("PlayerLeft11.png").convert())
             self.sprite_images_left.append(pygame.image.load("PlayerLeft12.png").convert())


             self.current_image_left = 0 #Count variable used for when the player is walking left
             

             self.image = pygame.image.load("PlayerRightStill.png").convert()

             self.rect=self.image.get_rect()

             
             self.rect.x=500 
             self.rect.y=700
             
             self.animate = 0 #Used to slow down the speed of animations
             
         def move(self,x,y):

             #Adds the movement values to the x and y of player
             self.x_speed += x
             self.y_speed += y

         def shoot(self):
            
            pos = pygame.mouse.get_pos()        #Get mouse position
            mouse_x = pos[0]                    #Get x coordinate of mouse position
            mouse_y = pos[1]                    #Get y coordinate of mouse position

            bullet = Bullet(mouse_x, mouse_y)
            bullet_list.add(bullet)
            all_sprites_list.add(bullet)
            
            if extrabullets_active == False:
                if len(bullet_list) > maxbullets:             #Makes it so that only 3 bullets can be on the screen at a time
                        bullet_list.remove(bullet)
                        all_sprites_list.remove(bullet)


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
        

            #Updating player images

            self.animate += 1 

            if self.animate % 6 == 0:                   #Update animation every 1 in 6 frames

                if self.x_speed > 0:
                
                    self.current_image_right += 1                                             #Add 1 to counter to loop through the array

                    self.image = self.sprite_images_right[self.current_image_right]                 #Set coin image to the current image in the array

                    if self.current_image_right >= (len(self.sprite_images_right) - 1):             #If the end of the array is reached, go back to the beginning
                        self.current_image_right = 0

                elif self.x_speed < 0:

                    self.current_image_left += 1                                             #Add 1 to counter to loop through the array

                    self.image = self.sprite_images_left[self.current_image_left]                 #Set coin image to the current image in the array

                    if self.current_image_left >= (len(self.sprite_images_left) - 1):             #If the end of the array is reached, go back to the beginning
                        
                        self.current_image_left = 0

                elif self.y_speed != 0:

                    self.current_image_right += 1                                             #Add 1 to counter to loop through the array

                    self.image = self.sprite_images_right[self.current_image_right]                 #Set coin image to the current image in the array

                    if self.current_image_right >= (len(self.sprite_images_right) - 1):             #If the end of the array is reached, go back to the beginning
                        self.current_image_right = 0
                    

                    

            
        
            


class Bullet(pygame.sprite.Sprite):                             #Creating bullet class
    def __init__(self,mouse_x,mouse_y):
        super().__init__()

        self.image = pygame.image.load("bullet.png").convert()  #Setting picture
        self.image.set_colorkey(BLACK)                          #Removing background
        self.rect = self.image.get_rect()

        self.damage = bullet_damage                             #This is a global variable used to assign the value, since it's needed permanently for scoreboards,



        speed = 5                                               #Set constant speed

        self.rect.x = player.rect.x         #Spawn it where the player is
        self.rect.y = player.rect.y 

        x_difference = (mouse_x - WIDTH/2)             #Calculate distance between mouse and player
        y_difference = (mouse_y - HEIGHT/2)            #for angle calculations below

        angle = math.atan2(y_difference, x_difference); #Works out gradient, and then the angle of the line
        self.x_change = math.cos(angle) * speed         #Multiply the angle with the speed the bullets travel at
        self.y_change = math.sin(angle) * speed
        self.x = self.rect.x                            #self.rect.x and self.rect.y are integers
        self.y = self.rect.y                            #this results in highly inaccurate aiming,
                                                        #the bullets don't go where the mouse is.
    def update(self):                                   #self.x and self.x are floating points
                                                        #which allows for more accuracy in calculations
        self.x += self.x_change
        self.y += self.y_change
        self.rect.x = int(self.x)                       #convert final answer back to integers
        self.rect.y = int(self.y)                       #since rect can't be float

class Enemy(pygame.sprite.Sprite):

    def __init__(self,x,y):

        super().__init__()

        if difficulty == 1:                 #If the user selects a higher difficulty,
            self.basehealth = 20                #Change enemy health to be higher
        elif difficulty == 2:
            self.basehealth = 30
        elif difficulty == 3:
            self.basehealth = 40
            
        self.score = 10
        self.damage = 5
        self.speed = 1
        self.distance = 0

        self.sprite_images_right = [] #Create list of images


        self.sprite_images_right.append(pygame.image.load("EnemyRight1.png").convert()) #Add all images to array
        self.sprite_images_right.append(pygame.image.load("EnemyRight2.png").convert())
        self.sprite_images_right.append(pygame.image.load("EnemyRight3.png").convert())
        self.sprite_images_right.append(pygame.image.load("EnemyRight4.png").convert())

        self.current_image_right = 0 #Count variable for when the enemy is moving right

        self.sprite_images_left = [] #Create list of images


        self.sprite_images_left.append(pygame.image.load("EnemyLeft1.png").convert()) #Add all images to array
        self.sprite_images_left.append(pygame.image.load("EnemyLeft2.png").convert())
        self.sprite_images_left.append(pygame.image.load("EnemyLeft3.png").convert())
        self.sprite_images_left.append(pygame.image.load("EnemyLeft4.png").convert())

        self.current_image_left = 0 #Count variable for when the enemy is moving left

        
        self.image = self.sprite_images_right[self.current_image_right] #Set default image for when it's still at the start

        self.image.set_colorkey(BLACK) #Remove background

        self.rect = self.image.get_rect()

        self.animate = 0 #Counter used to slow down the animation
        
        self.rect.x = x
        self.rect.y = y
        self.x_speed = 0
        self.y_speed = 0

        self.health = self.basehealth

    def update(self):

        self.animate += 1  #Add value every game tick, and only update every 6th tick to slow down the animation

        if self.animate % 6 == 0:                   #Update animation every 1 in 6 frames

            if self.x_speed < 0:
            
                self.current_image_right += 1                                             #Add 1 to counter to loop through the array

                self.image = self.sprite_images_right[self.current_image_right]                 #Set coin image to the current image in the array

                if self.current_image_right >= (len(self.sprite_images_right) - 1):             #If the end of the array is reached, go back to the beginning
                    self.current_image_right = 0

            elif self.x_speed > 0:

                self.current_image_left += 1                                             #Add 1 to counter to loop through the array

                self.image = self.sprite_images_left[self.current_image_left]                 #Set coin image to the current image in the array

                if self.current_image_left >= (len(self.sprite_images_left) - 1):             #If the end of the array is reached, go back to the beginning
                    
                    self.current_image_left = 0

            elif self.y_speed != 0:

                self.current_image_right += 1                                             #Add 1 to counter to loop through the array

                self.image = self.sprite_images_right[self.current_image_right]                 #Set coin image to the current image in the array

                if self.current_image_right >= (len(self.sprite_images_right) - 1):             #If the end of the array is reached, go back to the beginning
                    self.current_image_right = 0


class Spawner(pygame.sprite.Sprite):     #Spawners class

    def __init__(self,x,y):

        super().__init__()

        self.image = pygame.image.load("spawner.jpg").convert_alpha()
        self.image.set_colorkey(BLACK)
        self.rect=self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.health = 100
        self.damage = 30
        self.score = 30
        self.x_distance = 0
        self.y_distance = 0
        self.distance = 0
    

           
        



class Portal(pygame.sprite.Sprite):     #Portal class

    def __init__(self,x,y):

        super().__init__()

        self.image = pygame.image.load("nether.png").convert()  #Setting image
        self.rect=self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Coin(pygame.sprite.Sprite):

    def __init__(self,x,y):

        super().__init__()

        self.sprite_images = [] #Create list of images

        self.sprite_images.append(pygame.image.load("coin1.png").convert()) #Add all images to list
        self.sprite_images.append(pygame.image.load("coin2.png").convert())
        self.sprite_images.append(pygame.image.load("coin3.png").convert())
        self.sprite_images.append(pygame.image.load("coin4.png").convert())
        self.sprite_images.append(pygame.image.load("coin5.png").convert())
        self.sprite_images.append(pygame.image.load("coin6.png").convert())

        self.current_image = 0

        self.image = self.sprite_images[self.current_image]                 #Set current image as first image in array

        self.rect=self.image.get_rect() 
        self.image.set_colorkey(BLACK)                                      #Remove black background
        
        self.rect.x = x                                                     #Set coordinates
        self.rect.y = y

        self.animate = 0

    def update(self):

        self.animate += 1

        if self.animate % 4 == 0:
            
            self.current_image += 1                                             #Add 1 to counter to loop through the array

            self.image = self.sprite_images[self.current_image]                 #Set coin image to the current image in the array
            self.image.set_colorkey(BLACK)                                      #Remove black background for new image

            if self.current_image >= (len(self.sprite_images) - 1):             #If the end of the array is reached, go back to the beginning
                self.current_image = 0


class EnemyBullet(pygame.sprite.Sprite):

    def __init__(self,x,y):

        super().__init__()

        self.image = pygame.image.load("enemybullet.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.damage = 3
        

        self.speed = 8
        self.rect.x = x       #Make the bullet spawn where the player is at
        self.rect.y = y

        x_difference = player.rect.x - self.rect.x       #Calculate distance between player and enemy
        y_difference = player.rect.y - self.rect.y    #for angle calculations below

        self.angle = math.atan2(y_difference, x_difference); #Works out gradient, and then the angle of the line
        self.x_change = math.cos(self.angle) * self.speed         #Multiply the angle with
        self.y_change = math.sin(self.angle) * self.speed
        self.x = self.rect.x                            #self.rect.x and self.rect.y are integers
        self.y = self.rect.y                            #this results in highly inaccurate aiming,
                                                        #the bullets don't go where the mouse is.
    def update(self):                                   #self.x and self.x are floating points
                                                        #which allows for more accuracy in calculations
        self.x += self.x_change
        self.y += self.y_change
        self.rect.x = int(self.x)                       #convert final answer back to integers
        self.rect.y = int(self.y)                       #since rect can't be float


class Camera(pygame.sprite.Sprite):


    def __init__(self):
        
        super().__init__()
        
        self.camera = pygame.Rect(0,0,800,800)     #Sets a camera rectangle of size 800x800 (size of window)
                                           #Numbers keep track of how far the camera is from the start
        self.width = 800
        self.height = 800

    def movement(self, sprite):
         return sprite.rect.move(self.camera.topleft) #Moves the sprites around the same as the camera movement
                                                      #Starting point of camera is the top left corner
    def update(self, player):
        x = (player.rect.x*-1) + 400  #Keeps the player centered. Multiply by -1 because camera needs
        y = (player.rect.y*-1) + 400  #to move in oppposite direction to make it look like it's moving.

        self.camera = pygame.Rect(x,y, 800, 800)




#                     Powerups 

class AddHealth(pygame.sprite.Sprite):                          #AddHealth class for powerup used to give player health

    def __init__(self,x,y):

        super().__init__()

        self.addhealth = 10                                         #This is the health it adds to the player
        self.image=pygame.image.load("addhealth.png").convert()     #Setting image
        self.image.set_colorkey(BLACK)                              #Removing background
        self.rect=self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        
class ExtraDamage(pygame.sprite.Sprite):    #ExtraDamage class used to give player extra damage 

    def __init__(self,x,y):

        super().__init__()

        self.image=pygame.image.load("extradamage.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect=self.image.get_rect()
        self.rect.x = x
        self.rect.y = y



class ShieldPowerup(pygame.sprite.Sprite):  #This is the class for the icon that the player actually picks up to give it shield

    def __init__(self,x,y):

        super().__init__()

        self.image=pygame.image.load("shield_powerup.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect=self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class ExtraBullets(pygame.sprite.Sprite): #ExtraBullets class used to remove the limit on the number of bullets the player can shoot (temporarily)

    def __init__(self,x,y):

        super().__init__()

        self.image=pygame.image.load("extrabullets.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect=self.image.get_rect()
        self.rect.x = x
        self.rect.y = y



    


# --------------------------------------------------- #




# ---------------------- Functions ---------------------- #


# ------------------------------------------------------ #





# ------------- Pygame groups ------------- #
# ------------- Pygame lists ------------- #

all_sprites_list = pygame.sprite.Group()

player_list = pygame.sprite.Group()
player_hit_list = pygame.sprite.Group()

enemy_list = pygame.sprite.Group()
enemy_hit_list = pygame.sprite.Group()

enemy_bullet_list = pygame.sprite.Group()
enemy_bullet_hit_list = pygame.sprite.Group()

wall_list = pygame.sprite.Group()
wall_hit_list = pygame.sprite.Group()

bullet_list = pygame.sprite.Group()
bullet_hit_list = pygame.sprite.Group()

portal_list = pygame.sprite.Group()
portal_hit_list = pygame.sprite.Group()

coin_list = pygame.sprite.Group()
coin_hit_list = pygame.sprite.Group()

spawner_list = pygame.sprite.Group()
spawner_hit_list = pygame.sprite.Group()


            #Powerups

powerup_list = pygame.sprite.Group()

addhealth_list = pygame.sprite.Group()
addhealth_hit_list = pygame.sprite.Group()

extradamage_list = pygame.sprite.Group()
extradamage_hit_list = pygame.sprite.Group()

shield_powerup_list = pygame.sprite.Group()
shield_powerup_hit_list = pygame.sprite.Group()

extrabullets_list = pygame.sprite.Group()
extrabullets_hit_list = pygame.sprite.Group()


# ---------------------------------------- #
# ----------------------------------------- #




# Set the width and height of the screen [width, height]
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Fighter Game")
startscreen_image = pygame.image.load("background.jpg").convert()

extradamage_icon = pygame.image.load("extradamage.png").convert()
extradamage_icon.set_colorkey(BLACK)

extrabullets_icon = pygame.image.load("extrabullets.png").convert()
extrabullets_icon.set_colorkey(BLACK)

shield_icon = pygame.image.load("shield_powerup.png").convert()
shield_icon.set_colorkey(BLACK)



#Variables needed to be set before main loop

enemy_kills = 0 #Counter of how many enemies player has killed
coins_left = 0 #Variable used to see how 
level = 0


#Variables needed in timing calculations for different powerups


extradamage_start_time = 0  #Start timer of when powerup is collected       
extradamage_time_left = 0   #Variable used to see how long is left of a powerup before it's removed
extra_damage = False        #Boolean used to see whether a powerup is active or not

shield_powerup_start_time = 0
shield_powerup_time_left = 0
shield_powerup_active = False

extrabullets_start_time = 0
extrabullets_time_left = 0
extrabullets_active = False



directory = path.dirname(__file__) #Get the path to the file


#Boolean variables that need to be declared before main game loop

pausescreen = False
newlevel = False
pause = False
done = False
startscreen = True
powerup = False

howtoplay_screen = False
controls_screen = False
selectdifficulty_screen = False

#difficulty can't just be set to a random string, so I gave easy, medium, and hard
#number values for convenience and understandability of the code

easy = 1
medium = 2
hard = 3
maxbullets = 3

bullet_damage = 10

difficulty = hard


last_spawn = 0
# Used to manage how fast the screen updates
clock = pygame.time.Clock()


#Top

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:     #Making the player move.
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:     #If you want to go left, you -3 from the x coordinate.
                player.move(-3,0)
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player.move(3,0)
            elif event.key == pygame.K_UP or event.key == pygame.K_w:     #If you want to go up, you -3 from the y coordinate
                player.move(0,-3)
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                player.move(0,3)
            elif event.key == pygame.K_p:
                pausescreen = True
                player.x_speed = 0
                player.y_speed = 0

            elif event.key == pygame.K_SPACE:
                player.shoot()

        elif event.type == pygame.KEYUP:      #Making the player stop
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:    #Since you want the player to stop, you have to do the opposite
                player.move(3,0)              #action as above so that 0 gets added to the x or y
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player.move(-3,0)
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                player.move(0,3)
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                player.move(0,-3)

    #Saving highscore to textfile
    try:                                                #Try the following 3 lines of code:
        HIGHSCORE_FILE = open("highscore.txt", 'r')     #Open the file in read mode
        highscore = int(HIGHSCORE_FILE.read())          #Read the file and set whatever is inside equal to highscore
        HIGHSCORE_FILE.close()                          #Close the file
    except:
        highscore = 0                                   #If the code above doesn't work for some reason, set highscore to 0



    #---------------- Splash screen ---------------- #

    while startscreen == True:
        pause = True
        for event in pygame.event.get():        #Exit the startscreen if the user hits space
            if event.type == pygame.QUIT:
                startscreen = False
                done = True

        screen.fill(BLUE)


        play_button = pygame.Rect(200,200,400,400)                   #Create buttons. Rect(X,Y, Width, Height)            
        
        howtoplay_button = pygame.Rect(100,50,200,100)
        controls_button = pygame.Rect(500,50,200,100)
        selectdifficulty_button = pygame.Rect(250,650,300,100)


        pygame.draw.rect(screen, BLACK, play_button)                #Draw buttons on screen
        pygame.draw.rect(screen, ORANGE, howtoplay_button)
        pygame.draw.rect(screen, ORANGE, controls_button)
        pygame.draw.rect(screen, ORANGE, selectdifficulty_button)



        font = pygame.font.SysFont("Arial", 50) #Set font size and type
        
        #Set the text
        start_text = font.render("Slime Fighters", True, WHITE)         
        click_text= font.render("Click to Play", True, WHITE)
        hs_text = font.render("Highscore: " + str(highscore), True,WHITE)


        font = pygame.font.SysFont("Arial", 30)

        #Different font size for the smaller buttons
        howtoplay_text = font.render("How To Play", True, BLACK)
        controls_text = font.render("Controls", True, BLACK)
        selectdifficulty_text = font.render("Select Difficulty", True, BLACK)

    
        #Blit the text to the screen

        #Play button
        screen.blit(start_text, [400-(start_text.get_width() // 2), 250])
        screen.blit(click_text, [400-(click_text.get_width() // 2), 350])
        screen.blit(hs_text, [(400-hs_text.get_width() // 2), 450])

        #How to play, controls, select difficulty buttons
        screen.blit(howtoplay_text, [115, 80])
        screen.blit(controls_text, [543,80])
        screen.blit(selectdifficulty_text, [298, 680])



        #Collision with play button
        pos = pygame.mouse.get_pos()

        if play_button.collidepoint(pos):               #If mouse is hovering over the button,
            
            pygame.draw.rect(screen, GRAY, play_button)
            screen.blit(start_text, [400-(start_text.get_width() // 2), 250])
            screen.blit(click_text, [400-(click_text.get_width() // 2), 350])
            screen.blit(hs_text, [(400-hs_text.get_width() // 2), 450])
            
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN: #And is pressed, start the game
                    player = Player()
                    player_list.add(player)
                    all_sprites_list.add(player)
                    startscreen = False
                    pause = False

        #---------

                    
        #Collision with How To Play button
        if howtoplay_button.collidepoint(pos):
            pygame.draw.rect(screen, LIGHTORANGE, howtoplay_button) #If the mouse is hovering over the button, make the colour lighter to indicate that it is interactable
            screen.blit(howtoplay_text, [115, 80])
            

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    howtoplay_screen = True
                    
        #---------




        #Collision with Controls Button
        if controls_button.collidepoint(pos):

            pygame.draw.rect(screen, LIGHTORANGE, controls_button)  #If the mouse is hovering over the button, make the colour lighter to indicate that it is interactable
            screen.blit(controls_text, [543,80])
            
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    controls_screen = True

        #---------



        
        #Collision with Select Difficulty button
        if selectdifficulty_button.collidepoint(pos):

            pygame.draw.rect(screen, LIGHTORANGE, selectdifficulty_button)  #If the mouse is hovering over the button, make the colour lighter to indicate that it is interactable
            screen.blit(selectdifficulty_text, [298, 680])

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    selectdifficulty_screen = True
        

        pygame.display.update()

        #---------




        #-------------- Select Difficulty Screen ------------ #
        
        
        while selectdifficulty_screen == True:      #Only display the following when the select difficulty screen is enabled

            
            screen.fill(BLUE)                       #Set blue background

            #------
            
            back_button = pygame.Rect(500,650, 200, 100)    #Create buttons
            pygame.draw.rect(screen, ORANGE, back_button)   #Draw all the buttons on the screen


            easy_button = pygame.Rect(275,220,250,120)      
            pygame.draw.rect(screen, ORANGE, easy_button)

            medium_button = pygame.Rect(275,370,250,120)
            pygame.draw.rect(screen, ORANGE, medium_button)

            hard_button = pygame.Rect(275,520,250,120)
            pygame.draw.rect(screen, ORANGE, hard_button)

            
            #-------

            

            #-------
            
            font = pygame.font.SysFont("Arial", 50)         #Declare font
            
            if difficulty == 1:
                instruction_text = font.render("Select a difficulty. Current: Easy", True, WHITE)
            elif difficulty == 2:
                instruction_text = font.render("Select a difficulty. Current: Medium", True, WHITE)
            elif difficulty == 3:
                instruction_text = font.render("Select a difficulty. Current: Hard", True, WHITE)
            
            
            easy_text = font.render("Easy", True, WHITE)       #Set texts to be displayed on screen
            medium_text = font.render("Medium", True, WHITE)
            hard_text = font.render("Hard", True, WHITE)
            back_text = font.render("Back", True, BLACK)

            screen.blit(instruction_text, [400 - (instruction_text.get_width() // 2), 80])  #Display texts to screen
            screen.blit(easy_text, [400 - (easy_text.get_width() // 2), 250])
            screen.blit(medium_text, [400 - (medium_text.get_width() // 2), 400])
            screen.blit(hard_text, [400 - (hard_text.get_width() // 2), 550])
            screen.blit(back_text, [543, 670])
            
            
            #-------


            #-------
            
            pos = pygame.mouse.get_pos()                    #Get mouse position
            
            if back_button.collidepoint(pos):                       #Check whether the mouse is colliding (hovering over) the rectangle we created earlier
                pygame.draw.rect(screen, LIGHTORANGE, back_button)  #If it is hovering over, change the colour to a lighter shade to indicate it to the player
                screen.blit(back_text, [543, 670])                  #Re-blit the text over the colour so that it is seen, otherwise it's hidden underneath the new colour
                
            elif easy_button.collidepoint(pos):
                pygame.draw.rect(screen, LIGHTORANGE, easy_button)
                screen.blit(easy_text, [400 - (easy_text.get_width() // 2), 250])

            elif medium_button.collidepoint(pos):
                pygame.draw.rect(screen, LIGHTORANGE, medium_button)
                screen.blit(medium_text, [400 - (medium_text.get_width() // 2), 400])

            elif hard_button.collidepoint(pos):
                pygame.draw.rect(screen, LIGHTORANGE, hard_button)
                screen.blit(hard_text, [400 - (hard_text.get_width() // 2), 550])
                
            #-------
                
                
            for event in pygame.event.get():                #Event loop for clicking the buttons
                if event.type == pygame.QUIT:               #Quit game if user presses quit
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    
                    if back_button.collidepoint(pos):       #If the user clicks the back button, go off of the select difficulty screen
                        selectdifficulty_screen = False
                        
                    elif easy_button.collidepoint(pos):     #Set the value of difficulty depending on what the user clicks
                        difficulty = easy
                    elif medium_button.collidepoint(pos):
                        difficulty = medium
                    elif hard_button.collidepoint(pos):
                        difficulty = hard

            pygame.display.update()



        # ------------------- Controls Screen ------------------ #
        
        while controls_screen == True:

            screen.fill(BLUE)                               #Set blue background

            back_button = pygame.Rect(500,650, 200, 100)    #Create back button
            pygame.draw.rect(screen, ORANGE, back_button)   #Draw on screen
            
            font = pygame.font.SysFont("Arial", 40)         #Declare font

            
            left_text = font.render("Move Left: A or Left Arrow Key", True, WHITE)      #Set the value of the text for each line
            right_text = font.render("Move Right: D or Right Arrow Key", True, WHITE)
            up_text = font.render("Move Up: W or Up Arrow Key", True, WHITE)
            down_text = font.render("Move Down: S or Down Arrow Key", True, WHITE)
            shoot_text = font.render("Shoot bullets: Spacebar", True, WHITE)
            aim_text = font.render("Aim bullets: Mouse", True, WHITE)
            unpause_text = font.render("Pause or Unpause game: P", True, WHITE)

            back_text = font.render("Back", True, BLACK) #Back button

            screen.blit(left_text, [20, 50])            #Blit the text on screen at the corresponding coordinates
            screen.blit(right_text, [20, 150])
            screen.blit(down_text, [20, 250])
            screen.blit(shoot_text, [20, 350])
            screen.blit(aim_text, [20, 450])
            screen.blit(unpause_text, [20, 550])
            screen.blit(back_text, [554, 670])
            

            pos = pygame.mouse.get_pos()
            
            if back_button.collidepoint(pos):
                pygame.draw.rect(screen, LIGHTORANGE, back_button)  #If the mouse is hovering over the button, make the colour lighter to indicate that it is interactable
                screen.blit(back_text, [554, 670])
            

            for event in pygame.event.get():                #Event loop to see whether user is clicking a button
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:  #If user clicks,
                    if back_button.collidepoint(pos):       #and is hovering over the back button,
                        controls_screen = False             #go back from the current screen

            pygame.display.update()         #Update screen

        # -------------------------------------------------------- #


        # ------------------- How To Play Screen -------------------- #
        while howtoplay_screen == True:
            
            screen.fill(BLUE)                               #Set blue background

            back_button = pygame.Rect(500,650, 200, 100)    #Create back button
            pygame.draw.rect(screen, ORANGE, back_button)   #Draw on screen
            
            font = pygame.font.SysFont("Arial", 37)         #Declare font


            line_1 = font.render("To complete a level, you must kill all the", True, WHITE)     #Set the value of each line of text
            line_2 = font.render("enemies, and collect all the coins", True, WHITE)

            line_3 = font.render("Explore the map whilst avoiding the barrage", True, WHITE)
            line_4 = font.render("of projectiles that will hurt you!", True, WHITE)

            line_5 = font.render("Once a level is complete, go to the South-", True, WHITE)
            line_6 = font.render("East corner to purchase powerful upgrades", True, WHITE)
            line_7 = font.render("at the shop, or go through the portal to ", True, WHITE)
            line_8 = font.render("the next level", True, WHITE)

            line_9 = font.render("If you kill an enemy, you could get a powerup!", True, WHITE)
            line_10 = font.render("Collect it quickly to gain massive advantages", True, WHITE)
            line_11 = font.render("They will disappear if left too long!", True, WHITE)
            
            font = pygame.font.SysFont("Arial", 40)         #Declare font
            back_text = font.render("Back", True, BLACK)
        
            screen.blit(line_1, [20, 20])   #Blit each line of text to the screen
            screen.blit(line_2, [20, 70])
            
            screen.blit(line_3, [20, 145])
            screen.blit(line_4, [20, 195])
            
            screen.blit(line_5, [20, 270])
            screen.blit(line_6, [20, 320])
            screen.blit(line_7, [20, 370])
            screen.blit(line_8, [20, 420])
            
            screen.blit(line_9, [20, 495])
            screen.blit(line_10, [20, 545])
            screen.blit(line_11, [20, 595])
            
            screen.blit(back_text, [554, 670])  #Back button

            pos = pygame.mouse.get_pos() #Get mouse position

            if back_button.collidepoint(pos):
                pygame.draw.rect(screen, LIGHTORANGE, back_button)  #If the mouse is hovering over the button, make the colour lighter to indicate that it is interactable
                screen.blit(back_text, [554, 670])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN: #If the user clicks,
                    if back_button.collidepoint(pos):      #and is hovering over the back button,
                        howtoplay_screen = False           #Go back from the screen
                 
            pygame.display.update()     #Update screen

            

        # ----------------------------------------------------------------- #

    
    #Main game loop
        
    while pausescreen == True: #If the user has pressed the p key to pause,

     

        for event in pygame.event.get():        #Exit the startscreen if the user hits space
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pausescreen = False

        screen.fill(BLACK)                              #Display the screen
        font = pygame.font.SysFont("Arial", 50)
        pausetext = font.render("Game Paused, Press P to continue", True, WHITE, BLACK)
        screen.blit(pausetext, [400-(pausetext.get_width() //2), 300])
        pygame.display.update()






    # -------- Create level at the start of the game, and also if the player dies -------- #


    if level == 0 and pause == False: #If the game is started, and the player
        for coin in coin_list:
            coin_list.remove(coin)
        for enemy in enemy_list:
            enemy_list.remove(enemy)


        # KEY
        # 0 = Nothing
        # 1 = Wall
        # 2 = Enemy
        # 3 = Portal
        # 4 = Coins

        maps = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], #Setting maps array
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,1,1,1,1],
                [1,1,1,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,1,1,1,1],
                [1,1,1,1,0,0,1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,1,1,1,1,1],
                [1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,1,1,1,1,1],
                [1,1,1,1,0,0,4,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,1,1,1],
                [1,1,1,1,0,0,2,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,1,1,1],
                [1,1,1,1,0,0,0,0,0,0,1,1,1,1,0,0,1,0,0,0,0,0,1,1,1,1,1],
                [1,1,1,1,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,1,1,1,1,1,1,1,1],
                [1,1,1,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,1,1,1,1],
                [1,1,1,1,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,1,1,1,1],
                [1,1,1,1,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,1,1,1,1],
                [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,1,1,1],
                [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,1,1,1],
                [1,1,1,1,1,1,1,0,0,0,0,0,1,0,0,0,1,0,0,0,3,3,1,1,1,1,1],
                [1,1,1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,3,3,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]


        for y in range(24):                     #Looping through array to create walls
            for x in range(26):
                if maps[y][x] == 1:
                    wall=Wall(x*100, y*100)
                    all_sprites_list.add(wall)
                    wall_list.add(wall)

        for y in range(24):                     #Looping through array to create enemies
            for x in range(26):
                if maps[y][x] == 2:
                    enemy=Enemy(x*100, y*100)
                    all_sprites_list.add(enemy)
                    enemy_list.add(enemy)




        'Portal is created in while loop dependant on specific conditions'


        randomcoin = random.randrange(1,4)  ##Looping through array to create coins (1 in 4 chance)
        for y in range(24):
            for x in range(26):
                if maps[y][x] == 4:
                    coin=Coin(x*100, y*100)
                    all_sprites_list.add(coin)
                    coin_list.add(coin)

        maxbullets = 3
        bullet_damage = 10
        

                
        level += 1





    # ------------------------------------------------------------------------------------ #



    lastxpos = player.rect.x
    lastypos = player.rect.y

    all_sprites_list.update()

    camera = Camera()        #Create an instantiation of camera class
    camera.update(player)    #Update the camera so that the player moves around.



    # ------- Player Death ------ #

    if player.health <= 0:  #If player dies

        for event in pygame.event.get():        #Exit the startscreen if the user hits space
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    startscreen = True

        screen.blit(startscreen_image, [0,0])   #Background screen

        font = pygame.font.SysFont("Arial", 50) #Set value of death text
        death_text = font.render("You died", True, WHITE, BLACK)
        restart_text = font.render("Press space to go to the main menu", True, WHITE, BLACK)
        screen.blit(death_text, [400-(death_text.get_width() // 2), 300])                       #Display all the text to the screen
        screen.blit(restart_text, [400-(restart_text.get_width() // 2), 400])

        #Remove powerups
        shield_powerup_active = False
        extra_damage = False
        extrabullets_active = False



    #Remove all existing sprites
        for wall in wall_list:                  #Remove walls
            wall_list.remove(wall)
        for wall in all_sprites_list:
            all_sprites_list.remove(wall)

        for coin in coin_list:                  #Remove coins
            coin_list.remove(coin)
        for coin in coin_list:
            all_sprites_list.remove(coin)

        for enemy in enemy_list:                #Remove enemies
            enemy_list.remove(enemy)
        for enemy in all_sprites_list:
            all_sprites_list.remove(enemy)

        for bullet in bullet_list:              #Remove bullets
            bullet_list.remove(bullet)
        for bullet in all_sprites_list:
            bullet_list.remove(bullet)

        for spawner in spawner_list:            #Remove spawners
            spawner_list.remove(spawner)
        for spawner in all_sprites_list:
            all_sprites_list.remove(spawner)

        #Removing powerups in the rare occasion they spawn as the player dies
            
        for addhealth in addhealth_list:        #Remove add health powerup
            addhealth_list.remove(addhealth)
        for addhealth in all_sprites_list:
            all_sprites_list.remove(addhealth)
        for addhealth in powerup_list:
            powerup_list.remove(addhealth)


        for extradamage in extradamage_list:    #Remove extra damage powerup
            extradamage_list.remove(extradamage)
        for extradamage in all_sprites_list:
            all_sprites_list.remove(extradamage)
        for extradamage in powerup_list:
            powerup_list.remove(extradamage)
            

        for shield_powerup in shield_powerup_list:  #Remove shield powerup
            shield_powerup_list.remove(shield_powerup)
        for shield_powerup in all_sprites_list:
            all_sprites_list.remove(shield_powerup)
        for shield_powerup in powerup_list:
            powerup_list.remove(shield_powerup)
            

        for extrabullets in extrabullets_list:  #Remove extra bullets powerup
            extrabullets_list.remove(extrabullets)
        for extrabullets in all_sprites_list:
            all_sprites_list.remove(extrabullets)
        for extrabullets in powerup_list:
            powerup_list.remove(extrabullets)
            
        
        #Reset all player statistics for restart
        player_list.remove(player)
        all_sprites_list.remove(player)
        level = 0




        pygame.display.update()

    # --------------------------- #


                    # --- Collisions --- #

    # -------- Collision between bullet and wall -------- #


    for bullet in bullet_list:              #Remove bullet if it collides with wall
        if pygame.sprite.spritecollide(bullet, wall_list, False):
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)

    # --------------------------------------------------- #



    # -------- Collision between player and bullets ------- #


    #Player bullet collision with enemy
    for bullet in bullet_list:                                                  #If a bullet collides with enemy,
        enemy_hit_list = pygame.sprite.spritecollide(bullet, enemy_list, False) #Add to enemy_hit_list

        for enemy in enemy_hit_list:
            enemy.health -= bullet.damage       #Take away health from enemy and add score to player
            player.score += bullet.damage
            all_sprites_list.remove(bullet)     #Remove the bullet after collision
            bullet_list.remove(bullet)


    #Enemy bullet collision with wall
    for enemybullet in enemy_bullet_list:
        if pygame.sprite.spritecollide(enemybullet, wall_list, False):  #If enemy bullet collides with a wall, remove it
            all_sprites_list.remove(enemybullet)
            enemy_bullet_list.remove(enemybullet)

    #Enemy bullet collision with player

    player_hit_list = pygame.sprite.spritecollide(player, enemy_bullet_list, False)

    for enemybullet in player_hit_list:

        if shield_powerup_active == False:
            player.health -= enemybullet.damage
        all_sprites_list.remove(enemybullet)
        enemy_bullet_list.remove(enemybullet)
        player_hit_list.remove(enemybullet)



    # -------------------------------------------------------------- #

    # -------- Collision between player, bullets, and spawners ------- #
    
    for bullet in bullet_list:                                                          #If a bullet bullet collides with
        spawner_hit_list = pygame.sprite.spritecollide(bullet, spawner_list, False)     #a spawner, add to spawner_hit_list

        for spawner in spawner_hit_list:
            spawner.health -= bullet.damage     #Remove health from spawner
            player.score += bullet.damage       #Add score to player
            all_sprites_list.remove(bullet)     #Remove bullet 
            bullet_list.remove(bullet)


    player_hit_list = pygame.sprite.spritecollide(player, spawner_list, False)  #If a player collides with
                                                                                #a spawner, add to player_hit_list
    for spawner in player_hit_list:
        spawner.health -= player.damage     #Remove health from spawner
        player.health -= spawner.damage     #and player
        player.score += spawner.score       #Add score to player for damaging spawner






    # ------------------ Powerup Collisions ------------------ #

    
    #Addhealth powerup
        
    if len(addhealth_list) > 0:     #Only run code if the powerup is present (to reduce lag)

        addhealth_hit_list = pygame.sprite.spritecollide(player, addhealth_list, False)
            
        for addhealth in addhealth_hit_list:
            
            player.health += addhealth.addhealth
            all_sprites_list.remove(addhealth)
            powerup_list.remove(addhealth)
            addhealth_list.remove(addhealth)


    #-----------------



    #Extra damage powerup
            
    if len(extradamage_list) > 0:   #Only run code if the powerup is present (to reduce lag)
        
        extradamage_hit_list = pygame.sprite.spritecollide(player, extradamage_list, False)
                                       
         
        for extradamage in extradamage_hit_list:
            
            #Remove the collided sprite
            extradamage_list.remove(extradamage)                    
            powerup_list.remove(extradamage)
            all_sprites_list.remove(extradamage)

            #Set the start timer so that the powerup can remove itself later
            extradamage_start_time = pygame.time.get_ticks()

            #Set this variable to true, used for blitting the powerups on the screen so player can see which powerups are active
            extra_damage = True  

            #If the powerup is active,
            if extra_damage == True: 

                #Increase the bullet damage§
                bullet_damage += 10

               
    #Start the timer for how long it has left
    if extra_damage == True:
        extradamage_time_left = int((pygame.time.get_ticks() - extradamage_start_time) / 1000)

    #Once the powerup has reached the set time, reverse the extra damage
    if extradamage_time_left == 10:
        extra_damage = False

        bullet_damage -= 10
        extradamage_time_left = 0


    #-------------------

    if len(shield_powerup_list) > 0:    #Only run code if the powerup is present (to reduce lag)

        shield_powerup_hit_list = pygame.sprite.spritecollide(player, shield_powerup_list, False)

        

        for shield_powerup in shield_powerup_hit_list: #If the player collides with the powerup

            #Remove the collided sprite
            shield_powerup_list.remove(shield_powerup)  #Remove the powerup
            powerup_list.remove(shield_powerup)
            all_sprites_list.remove(shield_powerup)
            
            shield_powerup_start_time = pygame.time.get_ticks() #And start the timer

            shield_powerup_active = True

            #Set the start timer so that the powerup can remove itself later
            

    shield_powerup_time_left = (pygame.time.get_ticks() - shield_powerup_start_time) / 1000
    if shield_powerup_time_left > 10:
        
        shield_powerup_active = False
        shield_powerup_time_left = 0








    if len(extrabullets_list) > 0:

        extrabullets_hit_list = pygame.sprite.spritecollide(player, extrabullets_list, False)

        for extrabullets in extrabullets_hit_list:

            #Removed colllided powerup
            extrabullets_list.remove(extrabullets)
            powerup_list.remove(extrabullets)
            all_sprites_list.remove(extrabullets)

            extrabullets_start_time = pygame.time.get_ticks()

            extrabullets_active = True

    extrabullets_time_left = (pygame.time.get_ticks() - extrabullets_start_time) / 1000

    if extrabullets_time_left > 10:
        extrabullets_active = False
        extrabullets_time_left = 0

        

    # ------------- Coins and Coin collisions ------------- #

    player_hit_list = pygame.sprite.spritecollide(player, coin_list, False)

    for coin in player_hit_list:
        player.coins += 1
        coin_list.remove(coin)
        all_sprites_list.remove(coin)
        coins_left -= 1



    # ----------- Enemy movement, shooting at player wall collision, player collision ---------- #

    player_hit_list = pygame.sprite.spritecollide(player, enemy_list, False)

    for enemy in enemy_list:

        #Enemy x movement
        enemy.x_speed = player.rect.x-enemy.rect.x  #Calculate horizontal distance from player to enemy
        enemy.y_speed = player.rect.y-enemy.rect.y  #Calculate vertical distance
        enemy.distance = math.sqrt((enemy.x_speed**2) + (enemy.y_speed**2)) #Calculate actual distance using pythagorus' theorum
            
        if enemy.distance <= 600 and enemy.distance >= 400:         #Depending on distance, change speed
            enemy.rect.x += enemy.x_speed/400

        elif enemy.distance <= 400:
            enemy.rect.x += enemy.x_speed/200                       #The closer the enemy, the slower it'll go

        elif enemy.distance <= 50:
            enemy.x_speed = 0
                     

        #Enemy x wall collision
        for wall in wall_list:
            enemy_hit_list = pygame.sprite.spritecollide(wall, enemy_list, False)   #Same as player collision.

            for enemy in enemy_hit_list:                #If moving right and you hit a wall, set the right edge of the enemy to left edge of wall
                if enemy.x_speed > 0:                   #to stop it moving any further.
                    enemy.rect.right = wall.rect.left
                elif enemy.x_speed < 0:
                    enemy.rect.left = wall.rect.right


        #Enemy y movement
        if enemy.distance <= 600 and enemy.distance >= 600:                 #The X and Y movements must be done seperately to avoid huge glitches
            enemy.rect.y += enemy.y_speed/400                               #Calculating seperately allows for much smoother movement, and for the code to actual work

        elif enemy.distance <= 400:
            enemy.rect.y += enemy.y_speed/200

        elif enemy.distance <= 50:
            enemy.y_speed = 0

        #Enemy Y wall collision
        for wall in wall_list:
            enemy_hit_list = pygame.sprite.spritecollide(wall, enemy_list, False)

            for enemy in enemy_hit_list:

                if enemy.y_speed > 0:
                    enemy.rect.bottom = wall.rect.top
                elif enemy.y_speed < 0:
                    enemy.rect.top = wall.rect.bottom



        #Take health from both the enemy, and the player if they collide.
                    
        for enemy in player_hit_list:
            enemy.health -= player.damage
            if shield_powerup_active == False:
                player.health -= enemy.damage
            player.score += enemy.score

        if pygame.sprite.spritecollide(player, enemy_list, False):
           player.rect.x = lastxpos         #Bounce the player back if it collides with an enemy
           player.rect.y = lastypos

        enemyx = enemy.rect.x
        enemyy = enemy.rect.y
        playerx = player.rect.x
        playery = player.rect.y

        distance = math.sqrt((playerx-enemyx)**2 + (playery-enemyy)**2)  #Calculate distance from player to enemy in pixels using pythagorus
        
        if distance <= 600:                         #If player is within 400 pixels of enemy, enemy will shoot at player
            randomv = random.randint(1,20)          #Shoot on average twice a second
            if randomv == 1:
                enemybullet = EnemyBullet(enemy.rect.x+40, enemy.rect.y+20) #Makes bullet spawn in the middle of enemy
                enemy_bullet_list.add(enemybullet)
                all_sprites_list.add(enemybullet)




        #Enemy Death
                
        if enemy.health <= 0:       #Remove the enemy if it has died
            
            spawnpowerup = random.randint(1,5)                      #1 in 5 chance of spawning a powerup
            if spawnpowerup == 1:


                #Addhealth powerup
                randompowerup = random.randint(1,4)                 #Randomly choose which powerup is spawned
                
                if randompowerup == 1:                                #This powerup adds health to the enemy
                
                    addhealth = AddHealth(enemy.rect.x,enemy.rect.y)    #Create powerup where enemy died
                    
                    addhealth_list.add(addhealth)   #Add to lists
                    powerup_list.add(addhealth)
                    all_sprites_list.add(addhealth)
                    
                    addhealth_start_ticks = pygame.time.get_ticks() #Update the start of the timer
        
                #-----------------


                #Extra damage powerup
                elif randompowerup == 2:    #If the random powerup is 2, create an extra damage powerup

                    extradamage = ExtraDamage(enemy.rect.x,enemy.rect.y)    #Create powerup where enemy died

                    extradamage_list.add(extradamage)   #Add to lists
                    powerup_list.add(extradamage)
                    all_sprites_list.add(extradamage)

                    extradamage_start_ticks = pygame.time.get_ticks() #Start the timer so that it can be removed in 10 seconds

                # --------------------


                
                #Shield powerup
                elif randompowerup == 3:

                    shield_powerup = ShieldPowerup(enemy.rect.x, enemy.rect.y)             #Create powerup where enemy died

                    shield_powerup_list.add(shield_powerup) #Add to lists
                    powerup_list.add(shield_powerup)
                    all_sprites_list.add(shield_powerup)

                    shield_powerup_start_ticks = pygame.time.get_ticks()    #Start the timer so that it can be removed in 10 seconds

                # -------------------

                #Infinite bullets powerup
                elif randompowerup == 4:

                    extrabullets = ExtraBullets(enemy.rect.x, enemy.rect.y) #Create powerup where enemy died

                    extrabullets_list.add(extrabullets) #Add to lists
                    powerup_list.add(extrabullets)
                    all_sprites_list.add(extrabullets)

                    extrabullets_start_ticks = pygame.time.get_ticks()  #Start the timer so that it can be removed in 10 seconds
                
                
            
            #Remove the enemy after we get the coordinates                    
            all_sprites_list.remove(enemy)
            enemy_list.remove(enemy)
            enemy_kills += 1


    # ---------- Remove powerups from ground after they're 10 seconds old ---------- #
    
    seconds_alive_addhealth = 0
    seconds_alive_extradamage = 0
    seconds_alive_shield_powerup = 0
    seconds_alive_extrabullets = 0


    #Extra health
    
    for addhealth in addhealth_list:
        
        seconds_alive_addhealth = (pygame.time.get_ticks() - addhealth_start_ticks)/1000    #Get the time since the sprite has been created
            
        if seconds_alive_addhealth >= 10:                                         #If the powerup is left for more than 10 seconds
            
            addhealth_list.remove(addhealth)                                        #Remove it from the game
            powerup_list.remove(addhealth)
            all_sprites_list.remove(addhealth)


    #Extra damage
            
    for extradamage in extradamage_list:

        seconds_alive_extradamage = (pygame.time.get_ticks() - extradamage_start_ticks)/1000    #Get the time since the sprite has been created

        if seconds_alive_extradamage >= 10:                                         #If the powerup is left for more than 10 seconds
            
            extradamage_list.remove(extradamage)                                    #Remove it from the game
            powerup_list.remove(extradamage)
            all_sprites_list.remove(extradamage)


    #Shield

    for shield_powerup in shield_powerup_list:

        seconds_alive_shield = (pygame.time.get_ticks() - shield_powerup_start_ticks)/1000  #Get the time since the sprite has been created

        if seconds_alive_shield >= 10:                                              #If the powerup is left for more than 10 seconds
            
            shield_powerup_list.remove(shield_powerup)                              #Remove it from the game
            powerup_list.remove(shield_powerup)
            all_sprites_list.remove(shield_powerup)


    #Extra bullets
            
    for extrabullets in extrabullets_list:

        seconds_alive_extrabullets = (pygame.time.get_ticks() - extrabullets_start_ticks)/1000  #Get the time since the sprite has been created

        if seconds_alive_extrabullets >= 10:                                        #If the powerup is left for more than 10 seconds
            
            extrabullets_list.remove(extrabullets)                                  #Remove it from the game
            powerup_list.remove(extrabullets)
            all_sprites_list.remove(extrabullets)
            
            

    # ---------------------------------------------------------------------------------------------------------------- #

    
    
                
    # ------------------------- Next Levels ------------------------- #



    if len(enemy_list) == 0 and len(coin_list) == 0:  #If there are no enemies, coins (meaning player has beaten level), create new level
        
         oldhealth = player.health #Save old player stats before deleting them and making a new player instance
         oldscore = player.score
         oldkills = player.kills
         oldcoins = player.coins
         oldlevel = level

    

    
         if len(portal_list) == 0:
             for y in range(24):                         #Create portal at the desired location
                 for x in range(26):
                    if maps[y][x] == 3:
                        portal=Portal(x*100, y*100)      
                        all_sprites_list.add(portal)     #Add to lists
                        portal_list.add(portal)

         portal_hit_list = pygame.sprite.spritecollide(player, portal_list, False)  #Check for collisions between player and portal

         if len(portal_hit_list) != 0 and player.x_speed == 0 and player.y_speed == 0: #If there is a collision between the player and the portal 
                for wall in all_sprites_list:                                          #and the player is standing still
                    all_sprites_list.remove(wall)                                      #Begin removing everything from the current level
                for wall in wall_list:
                    wall_list.remove(wall)
                    all_sprites_list.remove(player)
                    player_list.remove(player)

                for bullet in bullet_list:
                    bullet_list.remove(bullet)
                for bullet in all_sprites_list:
                    all_sprites_list.remove(bullet)

                for portal in portal_list:      #Remove the portal once the player has collided with it
                    portal_list.remove(portal)  #So that it can be created in the next levels
                for portal in all_sprites_list:
                    all_sprites_list.remove(portal)
                for portal in portal_hit_list:
                    portal_list.remove(portal)

                for spawner in spawner_list:
                    spawner_list.remove(spawner)
                for spawner in all_sprites_list:
                    all_sprites_list.remove(spawner)
                for spawner in spawner_hit_list:
                    spawner_hit_list.remove(spawner)

                
                #Shop code

                shop = True

                while shop == True:
                    pause = True
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:       #If the player presses quit, exit all the loops
                                shop = False
                                pause = False
                                done = True

                    screen.fill(BLUE)

                    continue_button = pygame.Rect(550, 25, 200, 100)    #Create buttons
                    pygame.draw.rect(screen, ORANGE, continue_button)   #Draw on screens

                    
                    font = pygame.font.SysFont("Arial", 50) #Set font size and type
                    
                    shop_title_text = font.render("Shop", True, WHITE)  #Set title text



                    font = pygame.font.SysFont("Arial", 40) #Set font size and type

                    continue_text = font.render("Continue", True, BLACK)
                    
                    shop_text = font.render("Purchase permanent upgrades for the player", True, WHITE)      #Set explanation text
                    shop_text2 = font.render("Press the corresponding letters to purchase", True, WHITE)
                    shop_text3 = font.render("an upgrade", True, WHITE)


                    font = pygame.font.SysFont("Arial", 45) #Set font size and type
                    
                    upgrade_text = font.render("Upgrade", True, WHITE)  #Set subtitle txet
                    cost_text = font.render("Cost", True, WHITE)

                    exit_text = font.render("Exit", True, WHITE)
                    


                    font = pygame.font.SysFont("Arial", 40)
                    
                    A_text = font.render("A:    20 Health            -          100 Score", True, WHITE)    #Set information text
                    B_text = font.render("B:    +10 Damage       -          500 score", True, WHITE)
                    C_text = font.render("C:    +2 bullets            -          600 score", True, WHITE)


                    #Shows the value of the player attributes so he/she can see what to buy, and what he/she can buy
                    font = pygame.font.SysFont("Arial", 30)
                    text = font.render("Health: " + str(player.health) + " Score: " + str(player.score) + " Damage: " + str(bullet_damage) + " Bullets: " + str(maxbullets), True, WHITE)
                    #Display the user's current statistics to the screen
                    
                    screen.blit(shop_title_text, [(400 - (shop_title_text.get_width() // 2)), 20])  #Blit all the text to the screen

                    screen.blit(shop_text, [(400 - (shop_text.get_width() // 2)), 150])
                    screen.blit(shop_text2, [(400 - (shop_text.get_width() // 2)), 200])
                    screen.blit(shop_text3, [(400 - (shop_text.get_width() // 2)), 250])

                    screen.blit(upgrade_text, [(200 - (upgrade_text.get_width() // 2)), 350])
                    screen.blit(cost_text, [(600 - (cost_text.get_width() // 2)), 350])

                    screen.blit(A_text, [30, 450])
                    screen.blit(B_text, [30, 530])
                    screen.blit(C_text, [30, 610])

                    screen.blit(text, [(400 - (text.get_width() // 2)), 750])



                    #Continue Button allowing the user to move onto the next level
                    
                    screen.blit(continue_text, [570,53])

                    pos = pygame.mouse.get_pos()        #Get mouse position
                    
                    if continue_button.collidepoint(pos):
                        pygame.draw.rect(screen, LIGHTORANGE, continue_button) #If the mouse is hovering over the button, make the colour lighter to indicate that it is interactable
                        screen.blit(continue_text, [570, 53])

                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN: #If the button is pressed
                                shop = False                         #Start the game by exiting the loop
                                pause = False                        #and allowing sprites to update


                    #Shop Purchases

                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_a: #If the user presses A:
                                if player.score > 100:  #and has enough score to purchase the upgrade,
                                    player.health += 20 #Give the upgrade, and remove the score
                                    player.score -= 100

                            elif event.key == pygame.K_b: #If the user presses A:
                                if player.score > 500:  #and has enough score to purchase the upgrade,
                                    bullet_damage += 10 #Give the upgrade, and remove the score
                                    player.score -= 500

                            elif event.key == pygame.K_c: #If the user presses A:
                                if player.score > 600:  #and has enough score to purchase the upgrade,
                                    maxbullets += 2     #Give the upgrade, and remove the score
                                    player.score -= 600
                                
                            
                                

                    
                                

                    pygame.display.update()

                    
                                

                 # KEY
                 # 0 = Nothing
                 # 1 = Wall
                 # 2 = Enemy
                 # 3 = Portal
                 # 4 = Coins
                 # 5 = Player spawnpoint
                 # 6 = Enemy Spawners


                randommap = random.randint(1,4) #Randomises the map for each level


                if randommap == 1:

                    maps = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,0,1,0,0,0,0,2,0,0,2,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,2,0,1,0,0,0,0,0,0,6,0,0,2,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,4,0,0,1,1,1,1,1,0,0,0,0,4,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,2,0,0,0,0,0,0,2,0,0,0,0,0,6,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,4,0,0,0,1,0,0,2,0,0,2,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,0,0,2,0,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,6,0,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,2,0,0,0,1,0,0,0,0,0,0,4,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,0,0,0,0,6,0,0,0,0,0,0,0,2,0,1,1,1,1,1],
                            [1,1,1,1,0,0,1,1,1,1,1,0,0,2,0,0,0,0,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,6,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,2,0,6,2,0,0,1,0,2,0,0,2,0,0,0,0,3,3,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,3,3,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

                elif randommap == 2:

                    maps = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,2,0,0,0,0,0,0,2,0,0,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,0,0,0,0,1,0,0,2,0,0,0,0,2,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,2,0,0,0,0,1,0,6,2,0,4,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,6,0,4,0,0,2,0,1,0,0,2,0,0,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,0,0,0,2,1,0,0,0,0,0,0,2,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,4,0,0,0,1,0,0,0,0,0,2,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,0,0,0,6,1,0,0,0,0,4,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,6,0,2,0,2,0,2,1,0,0,6,0,2,0,0,3,3,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,3,3,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

                elif randommap == 3:

                    maps = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,1,0,0,2,0,1,0,0,0,0,2,1,0,6,0,1,1,1,1,1],
                            [1,1,1,1,0,0,2,1,0,6,2,0,1,0,0,0,0,0,1,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,1,0,0,0,0,1,0,0,6,0,0,1,0,2,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,1,1,1,1,1,1,0,0,0,0,0,1,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,4,0,0,0,2,0,0,0,2,0,0,0,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,1,1,0,0,4,0,0,0,0,1,1,1,1,1,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,2,0,1,1,1,1,1],
                            [1,1,1,1,0,0,2,1,1,1,1,1,1,1,1,0,0,0,4,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,2,0,6,0,1,1,1,1,1],
                            [1,1,1,1,0,6,0,1,1,1,1,0,0,0,1,2,0,0,2,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,0,2,1,0,0,0,1,0,0,6,0,0,3,3,1,1,1,1,1],
                            [1,1,1,1,0,0,2,0,4,0,0,0,0,2,0,0,0,0,0,0,3,3,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

                elif randommap == 4:

                    maps = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,0,0,0,1,0,0,2,0,0,0,0,0,0,2,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,1,0,4,0,0,0,0,0,0,0,0,0,0,2,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,1,0,0,2,0,0,0,1,0,0,0,1,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,1,0,6,0,0,0,0,1,0,0,0,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,1,1,0,0,1,1,0,0,0,4,0,1,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,6,0,0,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,0,2,4,0,0,0,0,0,0,2,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,1,1,0,0,0,0,2,0,0,1,1,1,1,1,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,2,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,1,1,0,0,0,1,1,1,0,2,0,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,6,0,2,0,0,0,0,1,1,1,1,0,2,0,0,1,1,1,1,1],
                            [1,1,1,1,0,2,0,1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,0,0,1,2,6,0,1,0,2,6,4,0,3,3,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,3,3,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]


                player = Player()   #Create new player
                player_list.add(player)
                all_sprites_list.add(player)    #Set new player attributes
                player.health = oldhealth       #As old player attributes
                player.score = oldscore         #So progress is saved
                player.kills = oldkills
                player.coins = oldcoins
                level = oldlevel + 1            #Add one to the level



                #Looping through map array to add in all walls
                for y in range(24):
                    for x in range(26):
                        if maps[y][x] == 1:
                            wall=Wall(x*100, y*100)
                            all_sprites_list.add(wall)
                            wall_list.add(wall)

                if difficulty != 3:

                    #Looping through map array to add in all enemies
                    for y in range(24):
                        for x in range(26):
                            if maps[y][x] == 2:
                                randomenemy = random.randint(1,4)   #Randomises number of enemies, and spawn locations
                                if randomenemy == 1:
                                    enemy=Enemy(x*100, y*100)
                                    all_sprites_list.add(enemy)
                                    enemy_list.add(enemy)

                 
                #Looping through map array to add in all walls
                for y in range(24):
                    for x in range(26):
                        if maps[y][x] == 4:
                            coin=Coin(x*100, y*100)
                            all_sprites_list.add(coin)
                            coin_list.add(coin)

                if difficulty == 3:     #If on hard difficulty
                    
                    for y in range(24):     #Loop through maps array
                        for x in range(26):
                            if maps[y][x] == 6:
                                randomspawner = random.randint(1,2) #1 in 2 chance of spawning a spawner
                                if randomspawner == 1:
                                    spawner=Spawner(x*100, y*100)   #Create spawner in location
                                    all_sprites_list.add(spawner)
                                    spawner_list.add(spawner)

                    while len(spawner_list) > 4:        #If there are too many spawners
                        spawner_list.remove(spawner)    #Remove a spawner until the limit is met
                        all_sprites_list.remove(spawner)
                        
                        
                        
                                        
                
                #Adds more health to enemy each level to make it harder as game progresse

                for enemy in enemy_list:
                    enemy.health += (level*2)

    # -------------------------------------------------------- #


    # ----------------- Hard Level ----------------------- #

    if difficulty == 3:
        
        for spawner in spawner_list:
            spawner.x_distance = player.rect.x - spawner.rect.x     #Find x distance between player and spawner
            spawner.y_distance = player.rect.y - spawner.rect.y     #Find y distance between player and spawner
            
            spawner.distance = math.sqrt((spawner.x_distance**2)+(spawner.y_distance**2))   #Find the actual distance
                                                                                            #between player and spawner

            current_ticks = pygame.time.get_ticks()     #Get the current time value
            if spawner.distance < 600 and len(enemy_list) < 10: #If there are less than 10 enemies + player within 600 pixels,
                

                if (current_ticks - last_spawn)/1000 > 5:   #Calculate the gap between the current time
                                                            # (current_ticks) and the last time an enemy was spawned in
                                                            # (last_spawn). If the gap is over 5 seconds, spawn a new enemy
                    
                    enemy=Enemy(spawner.rect.x, spawner.rect.y) #Spawn enemy at the spawner location
                    all_sprites_list.add(enemy)
                    enemy_list.add(enemy)

                    last_spawn = pygame.time.get_ticks()    #Get the time of which the last enemy was spawned in



            #Spawner Death

            if spawner.health <= 0:                 #If the spawner dies
                all_sprites_list.remove(spawner)    #Remove from map
                spawner_list.remove(spawner)
                player.score += 50                  #Give score to player
                 

                
            
    randomasd = random.randint(1,50)
    if randomasd == 1:
        print(len(spawner_list))
            
    # ----------------------------------------------------- #
            


    # ----------------- Displaying things on screen --------------- #

    
    ' -- Highscore + Player Scoreboard + Level information -- '
    if player.score > highscore:
        highscore = player.score

        try:                                                #Try to run the following 3 lines of code
            HIGHSCORE_FILE = open("highscore.txt", 'w')     #Open the highscore file in write mode
            HIGHSCORE_FILE.write(str(player.score))         #Write the highscore 
            HIGHSCORE_FILE.close()                          #Close the file
        except: 
            1 + 1                                           #If the code above doesn't work for some reason, just run this line instead


    if pause == False and player.health > 0:      #Only display if the player is alive and the game is playing
        screen.fill(BLACK)
        for sprite in all_sprites_list:                           #The same as all_sprites_list.draw, however now,
            
            screen.blit(sprite.image, camera.movement(sprite))  #we're drawing it compared to where the camera is rather than the window itself
            

                                                                #rather than the start screen
    

        #Create black bar behind information at bottom for clarity
        pygame.draw.line(screen, BLACK, [0,784],[800,784],50)
        
        #Displaying health, score, etc to user

        font = pygame.font.SysFont("hiraginosansgb", 30, True)
        text = font.render("Health: " + str(player.health) + " Score: " + str(player.score) + " Kills: " + str(enemy_kills) + " Coins: " + str(player.coins), True, WHITE)
        text_x = (400-(text.get_width() // 2))
        text_y = 768
        screen.blit(text, [text_x, text_y])    #Blitting scoreboard


        #Displaying level information to user
        font = pygame.font.SysFont("Aerial", 30, False, False)

        highscore_text = font.render("Highscore: " + str(highscore), False, WHITE)
        enemy_remain_text = font.render("Enemies Remaining: " + str(len(enemy_list)), False, WHITE)
        coin_remain_text = font.render("Coins Remaining: " + str(len(coin_list)), False, WHITE)

        font = pygame.font.SysFont("Aerial", 60, False, False)
        level_text = font.render("Level: " + str(level), False, WHITE)

        screen.blit(highscore_text, [0,0])
        screen.blit(enemy_remain_text, [0,30])
        screen.blit(coin_remain_text, [0,60])

        screen.blit(level_text, [(400 - (level_text.get_width() // 2)), 0])

        
        #If a powerup is active, display the icon on the top right to indicate to the player that it's active
        if extra_damage == True:
            screen.blit(extradamage_icon, [740, 0])

        if shield_powerup_active == True:
            screen.blit(shield_icon, [670, 0])

        if extrabullets_active == True:
            screen.blit(extrabullets_icon, [600, 0])
            
        
        




    pygame.display.flip()

    clock.tick(60)

    # --------------------------------------------------------------- #

# Close the window and quit.
pygame.quit()
