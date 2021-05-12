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
             self.health = 3000
             self.score = 1000
             self.kills = 0
             self.coins = 0
             self.damage = 5
             self.x_speed = 0
             self.y_speed = 0

             #Set player image and location

             self.sprite_images_right = [] #Create list of images

             self.sprite_images_right.append(pygame.image.load("PlayerRight1.png").convert()) #Add all images to list
             self.sprite_images_right.append(pygame.image.load("PlayerRight2.png").convert())
             self.sprite_images_right.append(pygame.image.load("PlayerRight3.png").convert())
             self.sprite_images_right.append(pygame.image.load("PlayerRight4.png").convert())
             self.sprite_images_right.append(pygame.image.load("PlayerRight5.png").convert())
             self.sprite_images_right.append(pygame.image.load("PlayerRight6.png").convert())
             self.sprite_images_right.append(pygame.image.load("PlayerRight7.png").convert())
             self.sprite_images_right.append(pygame.image.load("PlayerRight8.png").convert())
             self.sprite_images_right.append(pygame.image.load("PlayerRight9.png").convert())
             self.sprite_images_right.append(pygame.image.load("PlayerRight10.png").convert())
             self.sprite_images_right.append(pygame.image.load("PlayerRight11.png").convert())
             self.sprite_images_right.append(pygame.image.load("PlayerRight12.png").convert())

             self.current_image_right = 0


             self.sprite_images_left = []   #Create list of images

             self.sprite_images_left.append(pygame.image.load("PlayerLeft1.png").convert())
             self.sprite_images_left.append(pygame.image.load("PlayerLeft2.png").convert())
             self.sprite_images_left.append(pygame.image.load("PlayerLeft3.png").convert())
             self.sprite_images_left.append(pygame.image.load("PlayerLeft4.png").convert())
             self.sprite_images_left.append(pygame.image.load("PlayerLeft5.png").convert())
             self.sprite_images_left.append(pygame.image.load("PlayerLeft6.png").convert())
             self.sprite_images_left.append(pygame.image.load("PlayerLeft7.png").convert())
             self.sprite_images_left.append(pygame.image.load("PlayerLeft8.png").convert())
             self.sprite_images_left.append(pygame.image.load("PlayerLeft9.png").convert())
             self.sprite_images_left.append(pygame.image.load("PlayerLeft10.png").convert())
             self.sprite_images_left.append(pygame.image.load("PlayerLeft11.png").convert())
             self.sprite_images_left.append(pygame.image.load("PlayerLeft12.png").convert())


             self.current_image_left = 0
             

             self.image = pygame.image.load("PlayerRightStill.png").convert()

             self.rect=self.image.get_rect()

             
             self.rect.x=500
             self.rect.y=700
             
             self.animate = 0
             
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
                    

                    

            
        
            


class Bullet(pygame.sprite.Sprite):
    def __init__(self,mouse_x,mouse_y):
        super().__init__()

        self.image = pygame.image.load("bullet.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

        self.damage = bullet_damage



        speed = 5

        self.rect.x = player.rect.x
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

        self.current_image_right = 0

        self.sprite_images_left = [] #Create list of images


        self.sprite_images_left.append(pygame.image.load("EnemyLeft1.png").convert()) #Add all images to array
        self.sprite_images_left.append(pygame.image.load("EnemyLeft2.png").convert())
        self.sprite_images_left.append(pygame.image.load("EnemyLeft3.png").convert())
        self.sprite_images_left.append(pygame.image.load("EnemyLeft4.png").convert())

        self.current_image_left = 0

        
        self.image = self.sprite_images_right[self.current_image_right]

        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()

        self.animate = 0
        
        self.rect.x = x
        self.rect.y = y
        self.x_speed = 0
        self.y_speed = 0

        self.health = self.basehealth

    def update(self):

        self.animate += 1 

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


    
                

        
    
        



class Portal(pygame.sprite.Sprite):

    def __init__(self,x,y):

        super().__init__()

        self.image = pygame.image.load("nether.png").convert()
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

class AddHealth(pygame.sprite.Sprite):

    def __init__(self,x,y):

        super().__init__()

        self.health = 15
        self.addhealth = 10
        self.image=pygame.image.load("addhealth.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect=self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        
class ExtraDamage(pygame.sprite.Sprite):

    def __init__(self,x,y):

        super().__init__()

        self.health = 15
        self.image=pygame.image.load("extradamage.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect=self.image.get_rect()
        self.rect.x = x
        self.rect.y = y



class ShieldPowerup(pygame.sprite.Sprite):

    def __init__(self,x,y):

        super().__init__()

        self.health = 15
        self.image=pygame.image.load("shield_powerup.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect=self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class ShieldEffect(pygame.sprite.Sprite):

    def __init__(self,x,y):

        super().__init__()

        self.image=pygame.image.load("shield_effect.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect=self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class ExtraBullets(pygame.sprite.Sprite):

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


            #Powerups

powerup_list = pygame.sprite.Group()

addhealth_list = pygame.sprite.Group()
addhealth_hit_list = pygame.sprite.Group()

extradamage_list = pygame.sprite.Group()
extradamage_hit_list = pygame.sprite.Group()

shield_powerup_list = pygame.sprite.Group()
shield_powerup_hit_list = pygame.sprite.Group()

shield_effect_list = pygame.sprite.Group()
shield_effect_hit_list = pygame.sprite.Group()

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

enemy_kills = 0
coins_left = 0
level = 0
seconds_alive = 0


extradamage_start_time = 0
extradamage_time_left = 0
extra_damage = False

shield_powerup_start_time = 0
shield_powerup_time_left = 0
shield_powerup_active = False

extrabullets_start_time = 0
extrabullets_time_left = 0
extrabullets_active = False



directory = path.dirname(__file__) #Get the path to the file

pausescreen = False
newlevel = False
pause = False
done = False
startscreen = True
powerup = False

howtoplay_screen = False
controls_screen = False
selectdifficulty_screen = False


easy = 1
medium = 2
hard = 3
maxbullets = 3
bullet_damage = 10
difficulty = easy

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



        font = pygame.font.SysFont("Arial", 50)
        
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
            pygame.draw.rect(screen, ORANGE, back_button)   #Draw on screens


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
            
            if back_button.collidepoint(pos):
                pygame.draw.rect(screen, LIGHTORANGE, back_button)  #If the mouse is hovering over the button, make the colour lighter to indicate that it is interactable
                screen.blit(back_text, [543, 670])
                
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
                
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if back_button.collidepoint(pos):
                        selectdifficulty_screen = False
                        
                    elif easy_button.collidepoint(pos):
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

            
            left_text = font.render("Move Left: A or Left Arrow Key", True, WHITE)
            right_text = font.render("Move Right: D or Right Arrow Key", True, WHITE)
            up_text = font.render("Move Up: W or Up Arrow Key", True, WHITE)
            down_text = font.render("Move Down: S or Down Arrow Key", True, WHITE)
            shoot_text = font.render("Shoot bullets: Spacebar", True, WHITE)
            aim_text = font.render("Aim bullets: Mouse", True, WHITE)
            unpause_text = font.render("Pause or Unpause game: P", True, WHITE)

            back_text = font.render("Back", True, BLACK)

            screen.blit(left_text, [20, 50])
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
            

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if back_button.collidepoint(pos):
                        controls_screen = False

            pygame.display.update()

        # -------------------------------------------------------- #


        # ------------------- How To Play Screen -------------------- #

        
        while howtoplay_screen == True:
            
            screen.fill(BLUE)                               #Set blue background

            back_button = pygame.Rect(500,650, 200, 100)    #Create back button
            pygame.draw.rect(screen, ORANGE, back_button)   #Draw on screen
            
            font = pygame.font.SysFont("Arial", 37)         #Declare font


            line_1 = font.render("To complete a level, you must kill all the", True, WHITE)
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
        

            screen.blit(line_1, [20, 20])
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
            
            screen.blit(back_text, [554, 670])


            pos = pygame.mouse.get_pos()

            if back_button.collidepoint(pos):
                pygame.draw.rect(screen, LIGHTORANGE, back_button)  #If the mouse is hovering over the button, make the colour lighter to indicate that it is interactable
                screen.blit(back_text, [554, 670])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if back_button.collidepoint(pos):
                        howtoplay_screen = False
            

            pygame.display.update()

            

        # ----------------------------------------------------------------- #
        

    while pausescreen == True:

        for event in pygame.event.get():        #Exit the startscreen if the user hits space
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pausescreen = False

        screen.fill(BLACK)
        font = pygame.font.SysFont("Arial", 50)
        pausetext = font.render("Game Paused, Press P to continue", True, WHITE, BLACK)
        screen.blit(pausetext, [400-(pausetext.get_width() //2), 300])
        pygame.display.update()






    # -------- Create level at the start of the game, and also if the player dies -------- #


    if level == 0 and pause == False:
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

        maps = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
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


        for y in range(24):
            for x in range(26):
                if maps[y][x] == 1:
                    wall=Wall(x*100, y*100)
                    all_sprites_list.add(wall)
                    wall_list.add(wall)

        for y in range(24):
            for x in range(26):
                if maps[y][x] == 2:
                    enemy=Enemy(x*100, y*100)
                    all_sprites_list.add(enemy)
                    enemy_list.add(enemy)




        'Portal is created in while loop dependant on specific conditions'


        randomcoin = random.randrange(1,4)
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

    if player.health <= 0:

        for event in pygame.event.get():        #Exit the startscreen if the user hits space
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    startscreen = True

        screen.blit(startscreen_image, [0,0])

        font = pygame.font.SysFont("Arial", 50)
        death_text = font.render("You died", True, WHITE, BLACK)
        restart_text = font.render("Press space to go to the main menu", True, WHITE, BLACK)
        screen.blit(death_text, [400-(death_text.get_width() // 2), 300])
        screen.blit(restart_text, [400-(restart_text.get_width() // 2), 400])

        #Remove powerups
        shield_powerup_active = False
        extra_damage = False
        extrabullets_active = False



    #Remove all existing sprites
        for wall in wall_list:
            wall_list.remove(wall)
        for wall in all_sprites_list:
            all_sprites_list.remove(wall)

        for coin in coin_list:
            coin_list.remove(wall)
        for coin in coin_list:
            all_sprites_list.remove(coin)

        for enemy in enemy_list:
            enemy_list.remove(enemy)
        for enemy in all_sprites_list:
            all_sprites_list.remove(enemy)

        for bullet in bullet_list:
            bullet_list.remove(bullet)
        for bullet in all_sprites_list:
            bullet_list.remove(bullet)

        #Removing powerups in the rare occasion they spawn as the player dies
            
        for addhealth in addhealth_list:
            addhealth_list.remove(addhealth)
        for addhealth in all_sprites_list:
            all_sprites_list.remove(addhealth)
        for addhealth in powerup_list:
            powerup_list.remove(addhealth)


        for extradamage in extradamage_list:
            extradamage_list.remove(extradamage)
        for extradamage in all_sprites_list:
            all_sprites_list.remove(extradamage)
        for extradamage in powerup_list:
            powerup_list.remove(extradamage)
            

        for shield_effect in shield_effect_list:
            shield_effect_list.remove(shield)
        for shield_effect in all_sprites_list:
            all_sprites_list.remove(shield_effect)
        for shield_effect in powerup_list:
            powerup_list.remove(shield_effect)
            

        for shield_powerup in shield_powerup_list:
            shield_powerup_list.remove(shield_powerup)
        for shield_powerup in all_sprites_list:
            all_sprites_list.remove(shield_powerup)
        for shield_powerup in powerup_list:
            powerup_list.remove(shield_powerup)
            

        for extrabullets in extrabullets_list:
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
    


    # ------------------ Powerup Collisions ------------------ #

    
    #Addhealth powerup
        
    if len(addhealth_list) > 0:

        addhealth_hit_list = pygame.sprite.spritecollide(player, addhealth_list, False)
            
        for addhealth in addhealth_hit_list:
            
            player.health += addhealth.addhealth
            all_sprites_list.remove(addhealth)
            powerup_list.remove(addhealth)
            addhealth_list.remove(addhealth)


    #-----------------



    #Extra damage powerup
            
    if len(extradamage_list) > 0:
        
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

    i = random.randint(1,50)
    if i == 1:
        print(bullet_damage)

    #-------------------

    if len(shield_powerup_list) > 0:

        shield_powerup_hit_list = pygame.sprite.spritecollide(player, shield_powerup_list, False)

        

        for shield_powerup in shield_powerup_hit_list:

            #Remove the collided sprite
            shield_powerup_list.remove(shield_powerup)
            powerup_list.remove(shield_powerup)
            all_sprites_list.remove(shield_powerup)
            
            shield_powerup_start_time = pygame.time.get_ticks()

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
        if enemy.distance <= 600 and enemy.distance >= 400:                 #The X and Y movements must be done seperately to avoid huge glitches
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
            
            spawnpowerup = 1 #random.randint(1,5)                      #1 in 5 chance of spawning a powerup
            if spawnpowerup == 1:



                #Addhealth powerup
                randompowerup = 2 #random.randint(1,4)                 #Randomly choose which powerup is spawned
                
                if randompowerup == 1:                                #This powerup adds health to the enemy
                
                    addhealth = AddHealth(enemy.rect.x,enemy.rect.y)    #Create powerup where enemy died
                    
                    addhealth_list.add(addhealth)
                    powerup_list.add(addhealth)
                    all_sprites_list.add(addhealth)
                    
                    addhealth_start_ticks = pygame.time.get_ticks() #Update the start of the timer
        
                #-----------------


                #Extra damage powerup
                elif randompowerup == 2:

                    extradamage = ExtraDamage(enemy.rect.x,enemy.rect.y)    #Create powerup where enemy died

                    extradamage_list.add(extradamage)
                    powerup_list.add(extradamage)
                    all_sprites_list.add(extradamage)

                    extradamage_start_ticks = pygame.time.get_ticks()

                # --------------------


                
                #Shield powerup
                elif randompowerup == 3:

                    shield_powerup = ShieldPowerup(enemy.rect.x, enemy.rect.y)             #Create powerup where enemy died

                    shield_powerup_list.add(shield_powerup)
                    powerup_list.add(shield_powerup)
                    all_sprites_list.add(shield_powerup)

                    shield_powerup_start_ticks = pygame.time.get_ticks()

                # -------------------

                #Infinite bullets powerup
                elif randompowerup == 4:

                    extrabullets = ExtraBullets(enemy.rect.x, enemy.rect.y)

                    extrabullets_list.add(extrabullets)
                    powerup_list.add(extrabullets)
                    all_sprites_list.add(extrabullets)

                    extrabullets_start_ticks = pygame.time.get_ticks()
                
                
            
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
            
        if seconds_alive_addhealth >= 10:                                         #Remove the health powerup if it has been left for more than the set time
            
            addhealth_list.remove(addhealth)
            powerup_list.remove(addhealth)
            all_sprites_list.remove(addhealth)


    #Extra damage
            
    for extradamage in extradamage_list:

        seconds_alive_extradamage = (pygame.time.get_ticks() - extradamage_start_ticks)/1000

        if seconds_alive_extradamage >= 10:
            extradamage_list.remove(extradamage)
            powerup_list.remove(extradamage)
            all_sprites_list.remove(extradamage)


    #Shield

    for shield_powerup in shield_powerup_list:

        seconds_alive_shield = (pygame.time.get_ticks() - shield_powerup_start_ticks)/1000

        if seconds_alive_shield >= 10:
            
            shield_powerup_list.remove(shield_powerup)
            powerup_list.remove(shield_powerup)
            all_sprites_list.remove(shield_powerup)


    #Extra bullets
            
    for extrabullets in extrabullets_list:

        seconds_alive_extrabullets = (pygame.time.get_ticks() - extrabullets_start_ticks)/1000

        if seconds_alive_extrabullets >= 10:
            extrabullets_list.remove(extrabullets)
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
             for y in range(24):                         #Create portal
                 for x in range(26):
                    if maps[y][x] == 3:
                        portal=Portal(x*100, y*100)
                        all_sprites_list.add(portal)
                        portal_list.add(portal)

         portal_hit_list = pygame.sprite.spritecollide(player, portal_list, False)

         if len(portal_hit_list) != 0 and player.x_speed == 0 and player.y_speed == 0: #Remove everything from current level if the player goes into portal
                for wall in all_sprites_list:
                    all_sprites_list.remove(wall)
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

                
                #Shop

                shop = True

                while shop == True:
                    pause = True
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                shop = False
                                pause = False
                                done = True

                    screen.fill(BLUE)

                    continue_button = pygame.Rect(550, 25, 200, 100)    #Create buttons
                    pygame.draw.rect(screen, ORANGE, continue_button)   #Draw on screens

                    
                    font = pygame.font.SysFont("Arial", 50)
                    
                    shop_title_text = font.render("Shop", True, WHITE)



                    font = pygame.font.SysFont("Arial", 40)

                    continue_text = font.render("Continue", True, BLACK)
                    
                    shop_text = font.render("Purchase permanent upgrades for the player", True, WHITE)
                    shop_text2 = font.render("Press the corresponding letters to purchase", True, WHITE)
                    shop_text3 = font.render("an upgrade", True, WHITE)


                    font = pygame.font.SysFont("Arial", 45)
                    
                    upgrade_text = font.render("Upgrade", True, WHITE)
                    cost_text = font.render("Cost", True, WHITE)

                    exit_text = font.render("Exit", True, WHITE)
                    


                    font = pygame.font.SysFont("Arial", 40)
                    
                    A_text = font.render("A:    20 Health            -          100 Score", True, WHITE)
                    B_text = font.render("B:    +10 Damage       -          500 score", True, WHITE)
                    C_text = font.render("C:    +2 bullets            -          600 score", True, WHITE)

                    
                    font = pygame.font.SysFont("Arial", 30)
                    text = font.render("Health: " + str(player.health) + " Score: " + str(player.score) + " Damage: " + str(bullet_damage) + " Bullets: " + str(maxbullets), True, WHITE)
                    
                    screen.blit(shop_title_text, [(400 - (shop_title_text.get_width() // 2)), 20])

                    screen.blit(shop_text, [(400 - (shop_text.get_width() // 2)), 150])
                    screen.blit(shop_text2, [(400 - (shop_text.get_width() // 2)), 200])
                    screen.blit(shop_text3, [(400 - (shop_text.get_width() // 2)), 250])

                    screen.blit(upgrade_text, [(200 - (upgrade_text.get_width() // 2)), 350])
                    screen.blit(cost_text, [(600 - (cost_text.get_width() // 2)), 350])

                    screen.blit(A_text, [30, 450])
                    screen.blit(B_text, [30, 530])
                    screen.blit(C_text, [30, 610])

                    screen.blit(text, [(400 - (text.get_width() // 2)), 750])



                    #Continue Button
                    
                    screen.blit(continue_text, [570,53])

                    pos = pygame.mouse.get_pos()        #Get mouse position
                    
                    if continue_button.collidepoint(pos):
                        pygame.draw.rect(screen, LIGHTORANGE, continue_button) #If the mouse is hovering over the button, make the colour lighter to indicate that it is interactable
                        screen.blit(continue_text, [570, 53])

                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN: #And is pressed, start the game
                                shop = False
                                pause = False


                    #Shop Purchases

                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_a:
                                if player.score > 10:
                                    player.health += 20
                                    player.score -= 10

                            elif event.key == pygame.K_b:
                                if player.score > 50:
                                    bullet_damage += 10
                                    player.score -= 50

                            elif event.key == pygame.K_c:
                                if player.score > 60:
                                    maxbullets += 2
                                    player.score -= 60
                                    print('hi')
                                
                            
                                

                    
                                

                    pygame.display.update()

                    
                                

                 # KEY
                 # 0 = Nothing
                 # 1 = Wall
                 # 2 = Enemy
                 # 3 = Portal
                 # 4 = Coins
                 # 5 = Player spawnpoint


                randommap = random.randint(1,4)


                if randommap == 1:

                    maps = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,0,1,0,0,0,0,2,0,0,2,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,2,0,1,0,0,0,0,0,0,0,0,0,2,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,4,0,0,1,1,1,1,1,0,0,0,0,4,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,2,0,0,0,0,0,0,2,0,0,0,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,4,0,0,0,1,0,0,2,0,0,2,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,0,0,2,0,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,2,0,0,0,1,0,0,0,0,0,0,4,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,1,1,1,1,1],
                            [1,1,1,1,0,0,1,1,1,1,1,0,0,2,0,0,0,0,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,2,0,0,2,0,0,1,0,2,0,0,2,0,0,0,0,3,3,1,1,1,1,1],
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
                            [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,0,0,0,0,1,0,0,2,0,0,0,0,2,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,2,0,0,0,0,1,0,0,2,0,4,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,4,0,0,2,0,1,0,0,2,0,0,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,0,0,0,2,1,0,0,0,0,0,0,2,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,4,0,0,0,1,0,0,0,0,0,2,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,4,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,2,0,2,0,2,1,0,0,0,0,2,0,0,3,3,1,1,1,1,1],
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
                            [1,1,1,1,0,0,0,1,0,0,2,0,1,0,0,0,0,2,1,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,2,1,0,0,2,0,1,0,0,0,0,0,1,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,2,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,1,1,1,1,1,1,0,0,0,0,0,1,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,4,0,0,0,2,0,0,0,2,0,0,0,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,1,1,0,0,4,0,0,0,0,1,1,1,1,1,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,2,0,1,1,1,1,1],
                            [1,1,1,1,0,0,2,1,1,1,1,1,1,1,1,0,0,0,4,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,2,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,1,1,1,1,0,0,0,1,2,0,0,2,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,0,2,1,0,0,0,1,0,0,0,0,0,3,3,1,1,1,1,1],
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
                            [1,1,1,1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,1,1,0,0,1,1,0,0,0,4,0,1,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,0,2,4,0,0,0,0,0,0,2,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,1,1,0,0,0,0,2,0,0,1,1,1,1,1,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,2,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,1,1,0,0,0,1,1,1,0,2,0,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,0,2,0,0,0,0,1,1,1,1,0,2,0,0,1,1,1,1,1],
                            [1,1,1,1,0,2,0,1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,0,0,1,2,0,0,1,0,2,0,4,0,3,3,1,1,1,1,1],
                            [1,1,1,1,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,3,3,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]


                player = Player()
                player_list.add(player)
                all_sprites_list.add(player)
                player.health = oldhealth
                player.score = oldscore
                player.kills = oldkills
                player.coins = oldcoins
                level = oldlevel + 1



                #Adding in features for new levels
                for y in range(24):
                    for x in range(26):
                        if maps[y][x] == 1:
                            wall=Wall(x*100, y*100)
                            all_sprites_list.add(wall)
                            wall_list.add(wall)


                for y in range(24):
                    for x in range(26):
                        if maps[y][x] == 2:
                            randomenemy = random.randint(1,4)
                            if randomenemy == 1:
                                enemy=Enemy(x*100, y*100)
                                all_sprites_list.add(enemy)
                                enemy_list.add(enemy)

                for y in range(24):
                    for x in range(26):
                        if maps[y][x] == 4:
                            coin=Coin(x*100, y*100)
                            all_sprites_list.add(coin)
                            coin_list.add(coin)


                #Adds more health to enemy each level to make it harder

                for enemy in enemy_list:
                    enemy.health += (level*2)

    # -------------------------------------------------------- #

    for enemybullet in enemy_bullet_list:
        enemybullet.damage += (level*2)

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
    

        pygame.draw.line(screen, BLACK, [0,784],[800,784],50)
        #Displaying health, score, etc to user

        font = pygame.font.SysFont("hiraginosansgb", 30, True)
        text = font.render("Health: " + str(player.health) + " Score: " + str(player.score) + " Kills: " + str(enemy_kills) + " Coins: " + str(player.coins), True, WHITE)
        text_x = (400-(text.get_width() // 2))
        text_y = 768
        screen.blit(text, [text_x, text_y])    #Blitting scoreboard

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
